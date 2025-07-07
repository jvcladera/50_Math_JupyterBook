import os
import shutil

# --- Rutas --- #
original_chapters_long_dir = r"C:\Users\pc-57\Desktop\Code\50_Math\data\chapters_long"
jupyterbook_root_dir = r"C:\Users\pc-57\Desktop\Code\50_Math_JupyterBook\MathBook"
jupyterbook_chapters_content_dir = os.path.join(jupyterbook_root_dir, "chapters_content")

# --- Contenido de _toc.yml --- #
toc_content = """
format: jb-book
root: intro.md
chapters:
- file: chapters_content/00_Introduction
- file: chapters_content/01_Zero
- file: chapters_content/02_Number_systems
- file: chapters_content/03_Fractions
- file: chapters_content/04_Squares_and_square_roots
- file: chapters_content/05_Pi
- file: chapters_content/06_e
- file: chapters_content/07_Infinity
- file: chapters_content/08_Imaginary_numbers
- file: chapters_content/09_Primes
- file: chapters_content/10_Perfect_numbers
- file: chapters_content/11_Fibonacci_numbers
- file: chapters_content/12_Golden_rectangles
- file: chapters_content/13_Pascals_triangle
- file: chapters_content/14_Algebra
- file: chapters_content/15_Euclids_algorithm
- file: chapters_content/16_Logic
- file: chapters_content/17_Proof
- file: chapters_content/18_Sets
- file: chapters_content/19_Calculus
- file: chapters_content/20_Constructions
- file: chapters_content/21_Triangles
- file: chapters_content/22_Curves
- file: chapters_content/23_Topology
- file: chapters_content/24_Dimension
- file: chapters_content/25_Fractals
- file: chapters_content/26_Chaos
- file: chapters_content/27_The_parallel_postulate
- file: chapters_content/28_Discrete_geometry
- file: chapters_content/29_Graphs
- file: chapters_content/30_The_four-colour_problem
- file: chapters_content/31_Probability
- file: chapters_content/32_Bayess_theory
- file: chapters_content/33_The_birthday_problem
- file: chapters_content/34_Distributions
- file: chapters_content/35_The_normal_curve
- file: chapters_content/36_Connecting_data
- file: chapters_content/37_Genetics
- file: chapters_content/38_Groups
- file: chapters_content/39_Matrices
- file: chapters_content/40_Codes
- file: chapters_content/41_Advanced_counting
- file: chapters_content/42_Magic_squares
- file: chapters_content/43_Latin_squares
- file: chapters_content/44_Money_mathematics
- file: chapters_content/45_The_diet_problem
- file: chapters_content/46_The_travelling_salesperson
- file: chapters_content/47_Game_theory
- file: chapters_content/48_Relativity
- file: chapters_content/49_Fermats_last_theorem
- file: chapters_content/50_The_Riemann_hypothesis
- file: chapters_content/51_Glossary
"""

# --- Contenido de _config.yml --- #
config_content = """
# Book settings
# Learn more at https://jupyterbook.org/customize/config.html

title: 50 Mathematical Ideas You Really Need to Know
author: Tony Crilly (Adapted by Gemini)
logo: logo.png

# Force re-execution of notebooks on each build.
# See https://jupyterbook.org/content/execute.html
execute:
  execute_notebooks: auto  # auto, force, cache, off
  allow_errors: true       # Permitir errores en la ejecución de celdas

# Define the name of the latex output file for PDF builds
latex:
  latex_documents:
    targetname: book.tex

# Add a bibtex file so that we can create citations
bibtex_bibfiles:
  - references.bib

# Information about where the book exists on the web
repository:
  url: https://github.com/executablebooks/jupyter-book  # Online location of your book
  path_to_book: docs  # Optional path to your book, relative to the repository root
  branch: master  # Which branch of the repository should be used when creating links (optional)

# Add GitHub buttons to your book
# See https://jupyterbook.org/customize/config.html#add-a-link-to-your-repository
html:
  use_issues_button: true
  use_repository_button: true
root: intro.md
"""

# --- Funciones --- #
def clean_directory(directory):
    if os.path.exists(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    os.makedirs(directory, exist_ok=True)

def copy_and_rename_chapters():
    clean_directory(jupyterbook_chapters_content_dir)
    
    chapter_dirs = sorted([d for d in os.listdir(original_chapters_long_dir) if os.path.isdir(os.path.join(original_chapters_long_dir, d))])

    for chapter_dir in chapter_dirs:
        source_file_path = os.path.join(original_chapters_long_dir, chapter_dir, "content.md")
        destination_file_name = f"{chapter_dir}.md"
        destination_file_path = os.path.join(jupyterbook_chapters_content_dir, destination_file_name)
        
        if os.path.exists(source_file_path):
            shutil.copyfile(source_file_path, destination_file_path)
            print(f"Copied: {source_file_path} to {destination_file_path}")
        else:
            print(f"Source file not found: {source_file_path}")

def write_config_files():
    with open(os.path.join(jupyterbook_root_dir, "_toc.yml"), "w", encoding="utf-8") as f:
        f.write(toc_content)
    print("Updated _toc.yml")

    with open(os.path.join(jupyterbook_root_dir, "_config.yml"), "w", encoding="utf-8") as f:
        f.write(config_content)
    print("Updated _config.yml")

    # Create a simple intro.md if it doesn't exist
    intro_path = os.path.join(jupyterbook_root_dir, "intro.md")
    if not os.path.exists(intro_path):
        with open(intro_path, "w", encoding="utf-8") as f:
            f.write("# Introducción a 50 Ideas Matemáticas\n\nBienvenido a la versión interactiva de \"50 Ideas Matemáticas que Realmente Necesitas Conocer\".\n\nEste libro explora conceptos fundamentales de las matemáticas, desde los números hasta la teoría de juegos, con ejemplos interactivos en Python para una mejor comprensión.\n\n¡Esperamos que disfrutes tu viaje a través del fascinante mundo de las matemáticas!")
        print("Created intro.md")

# --- Ejecución --- #
if __name__ == "__main__":
    print("Starting JupyterBook setup...")
    copy_and_rename_chapters()
    write_config_files()
    print("JupyterBook setup complete. Now run 'jupyter-book build .' from the JupyterBook root directory.")
