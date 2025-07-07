# Project: 50 Mathematical Ideas You Really Need to Know - Interactive Reader

This project is a Flask web application that serves as an interactive reader for the book "50 Mathematical Ideas You Really Need to Know".

## Key Information:

*   **Purpose:** To provide a web-based interface for reading the book, with interactive navigation, and to make the app interactive with Python code to better understand the book.
*   **Technology Stack:** Python, Flask, HTML, CSS.
*   **Content Source:** The book content is extracted from a text file (`50_idea_v1_summary.md`) located in the `data` directory.
*   **Main Application File:** `math_app/app.py`
*   **Content Parsing Logic:** `math_app/summary_parser.py`
*   **Entry Point:** `main.py` (runs the Flask application)
*   **Static Assets:** `math_app/static/style.css`
*   **Templates:** `math_app/templates/chapter.html`, `math_app/templates/index.html`
*   **Data Files:** The `data` directory contains various formats of the book, including `.md`, `.epub`, and `.pdf`. The application primarily uses the `.md` file for content extraction.

## How to Run:

1.  **Navigate to the project root:** `cd C:\Users\pc-57\Desktop\Code\50_Math`
2.  **Install dependencies:** `pip install Flask`
3.  **Run the application:** `py main.py`
4.  **Access in browser:** Open `http://127.0.0.1:5000/`

## Important Notes:

*   The `run_code` functionality in `app.py` should be handled with caution due to potential security risks, especially in production environments.
*   The application now uses the summarized content from `50_idea_v1_summary.md`.

## Common Tasks:

*   **Updating Book Content:** Modify the `50_idea_v1.md` file in the `data` directory and re-run the summarization process.
*   **Modifying UI/UX:** Edit `math_app/static/style.css` for styling and `math_app/templates/*.html` for structure.
*   **Adding New Features:** Implement logic in `math_app/app.py` and `math_app/summary_parser.py`.
