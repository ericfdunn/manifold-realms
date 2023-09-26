import os

# Define the function to generate the TOC
def generate_toc(directory, root_directory, indent_level=0):
    toc = ""
    if indent_level==0:
        toc = "## Table of Contents \n"
   # files = []
    folders = []

    # List all items (files and directories) in the current directory
    items = os.listdir(directory)

    # Sort items alphabetically
    items.sort()

    for item in items:
        item_path = os.path.join(directory, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            folders.append(item)

        # Check if the item is a Markdown file
        if item.endswith(".md") and not item.startswith((".", "!", "$")):
            # Create a relative hyperlink
            relative_path = os.path.relpath(item_path, root_directory)
            toc += f"- [{item.replace('.md', '')}](<{relative_path}>)\n"

    # Generate headings for folders
    for folder in folders:
        if not folder.startswith((".", "!", "$")):
            toc += f"###{'#' * indent_level} {folder}\n"
            folder_path = os.path.join(directory, folder)
            toc += generate_toc(folder_path, root_directory, indent_level + 1)

    return toc

if __name__ == "__main__":
    # Get the current directory
    current_directory = os.getcwd()

    # Generate the TOC starting from the current directory
    table_of_contents = generate_toc(current_directory, current_directory)

    # Print the generated TOC
    print(table_of_contents)

