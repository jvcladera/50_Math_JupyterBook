
# 50 Mathematical Ideas You Really Need to Know - Interactive Book (JupyterBook)

This project transforms the book "50 Mathematical Ideas You Really Need to Know" into an interactive web book using JupyterBook. It combines explanatory text with executable Python code and visualizations, offering an enriched learning experience.

## Key Features:

- **Interactive Content**: Chapters include detailed explanations and Python code blocks that can be executed directly in the browser.
- **Integrated Visualizations**: Python code examples can generate charts and visualizations that are embedded directly in the book's content.
- **Structured Navigation**: Organized as a web book with a table of contents, search, and chapter navigation.
- **Markdown and Notebook-Based**: The content is written in Markdown, and code examples are integrated natively.

## Project Structure:

```
50_Math_JupyterBook/
├── _build/                                    # Directory where the static website is generated
│   └── html/
├── data/
│   ├── 50_idea_v1.md
│   └── 50_idea_v1_summary.md
├── MathBook/
│   ├── _config.yml                            # Global book configuration (title, author, etc.)
│   ├── _toc.yml                               # Defines the book structure and chapter order
│   ├── intro.md                               # Introduction page of the book
│   └── chapters_content/                      # Directory for chapter content files
│       ├── 00_Introduction.md
│       ├── 01_Zero.md
│       └── ...
├── build.bat                                  # Easy build script for Windows
├── GEMINI.md                                  # Project documentation for Gemini
└── README.md                                  # This file
```

## How to Build the Book:

1.  **Prerequisites:**
    *   Python 3.x
    *   `jupyter-book` installed (`pip install jupyter-book`)

2.  **Build the book:**
    *   Simply run the `build.bat` script by double-clicking it or by running it from your terminal:
        ```bash
        build.bat
        ```

3.  **View the book:**
    *   Once the build is complete, open the `_build/html/index.html` file in your web browser.

