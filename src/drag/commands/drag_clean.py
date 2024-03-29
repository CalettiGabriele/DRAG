import sys
import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell

def check_cell_for_comments(cell: nbformat.notebooknode.NotebookNode, comments: list):
    if cell.cell_type == 'markdown':
        return True
    elif cell.cell_type == 'code':
        return any(comment in line for line in cell.source.split('\n') for comment in comments if line.strip())
    return False

def remove_cells_without_comments(notebook: nbformat.NotebookNode, comments: list):
    new_cells = [cell for cell in notebook.cells if check_cell_for_comments(cell, comments)]
    notebook.cells = new_cells

def main():
    if len(sys.argv) != 2:
        print("Usage: python drag_clean.py <path_to_notebook.ipynb>")
        sys.exit(1)

    ipynb_path = sys.argv[1]
    with open(ipynb_path, 'r') as f:
        notebook = nbformat.read(f, as_version=4)

    comments_to_keep = ['# Code generated by DRAG',
                        '#Code generated by DRAG',
                        '# DRAG',
                        '#DRAG',
                        ]
    remove_cells_without_comments(notebook, comments_to_keep)

    new_ipynb_path = ipynb_path.replace('.ipynb', '_cleaned.ipynb')
    with open(new_ipynb_path, 'w') as f:
        nbformat.write(notebook, f)


if __name__ == "__main__":
    main()