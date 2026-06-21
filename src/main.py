from textnode import TextNode, TextType
import os
import shutil
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode
from pathlib import Path
import sys

def copy_files_recursive(source_dir_path, dest_dir_path):
    # 1. Make sure the destination exists (create it fresh)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # 2. List everything in the source directory
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")

        # 3. If it's a file, copy it. If it's a directory, recurse.
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def copy_files(source_dir_path, dest_dir_path, basepath):
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)
    os.mkdir(dest_dir_path)
    copy_files_recursive(source_dir_path, dest_dir_path)
    generate_pages_recursive("content", "template.html", "docs", basepath)



dir_path_static = "./static"
dir_path_public = "./docs"

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[:2] == "# ":
            line = line.lstrip("# ")
            line = line.lstrip()
            return line
    raise ValueError("No H1 Header!")

def generate_page(from_path, template_path, dest_path, basepath):
    print("Generating page from from_path to dest_path using template_path")
    markdown_file = ""
    template_file = ""
    with open(from_path, "r") as file:
        markdown_file = file.read()
    with open(template_path, "r") as file:
        template_file = file.read()

    html_string = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)

    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", html_string)
    # Handle double quotes
    template_file = template_file.replace('href="/', 'href="' + basepath)
    template_file = template_file.replace('src="/', 'src="' + basepath)

    # Handle single quotes just in case
    template_file = template_file.replace("href='/", "href='" + basepath)
    template_file = template_file.replace("src='/", "src='" + basepath)

    file_path = Path(dest_path)

    # 3. Create missing parent directories automatically
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # 4. Write the HTML content using UTF-8 encoding
    file_path.write_text(template_file, encoding="utf-8")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir = os.listdir(dir_path_content)
    for d in dir:
        full_path = os.path.join(dir_path_content, d)
        if os.path.isfile(full_path):
            generate_page(full_path, template_path, os.path.join(dest_dir_path, Path(d).with_suffix(".html")), basepath)
        else:
            generate_pages_recursive(full_path, template_path, os.path.join(dest_dir_path, d), basepath)

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    copy_files(dir_path_static, dir_path_public, basepath)

main()