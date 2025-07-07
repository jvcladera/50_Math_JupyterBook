@echo OFF
echo Building the Jupyter Book...

REM Navigate to the root directory of the project
cd /D "%~dp0"

REM Execute the jupyter-book build command
call "C:\Users\pc-57\AppData\Local\Programs\Python\Python313\Scripts\jupyter-book.exe" build MathBook --all

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred while building the Jupyter Book.
) ELSE (
    echo.
    echo Jupyter Book built successfully!
    echo You can find the generated website in: _build\html\index.html
)

pause
