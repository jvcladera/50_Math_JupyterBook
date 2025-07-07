# 50 Mathematical Ideas You Really Need to Know - Interactive Book (JupyterBook)

Este proyecto transforma el libro "50 Mathematical Ideas You Really Need to Know" en un libro web interactivo utilizando JupyterBook. Combina texto explicativo con código Python ejecutable y visualizaciones, ofreciendo una experiencia de aprendizaje enriquecida.

## Características Principales:

-   **Contenido Interactivo**: Los capítulos incluyen explicaciones detalladas y bloques de código Python que pueden ser ejecutados directamente en el navegador (a través de Thebe, si está configurado).
-   **Visualizaciones Integradas**: Los ejemplos de código Python pueden generar gráficos y visualizaciones que se incrustan directamente en el contenido del libro.
-   **Navegación Estructurada**: Organizado como un libro web con tabla de contenidos, búsqueda y navegación entre capítulos.
-   **Basado en Markdown y Notebooks**: El contenido se escribe en Markdown y los ejemplos de código se integran de forma nativa.

## Estructura del Proyecto (JupyterBook):

```
50_Math_JupyterBook/MathBook/
├── _config.yml                                # Configuración global del libro (título, autor, etc.)
├── _toc.yml                                   # Define la estructura del libro y el orden de los capítulos
├── intro.md                                   # Página de introducción del libro
├── GEMINI.md                                  # Documentación del proyecto original (copia)
├── README.md                                  # README del proyecto original (copia)
├── chapters_content/                          # Directorio para los archivos de contenido de los capítulos
│   ├── 00_Introduction.md
│   ├── 01_Zero.md
│   │   ...
│   └── 51_Glossary.md
└── _build/                                    # Directorio donde se genera el sitio web estático
    └── html/
        └── ...
```

## Configuración y Ejecución (JupyterBook):

Sigue estos pasos para configurar y construir el libro web en tu entorno local:

### Prerrequisitos:

-   Python 3.x
-   pip (gestor de paquetes de Python)
-   `jupyter-book` instalado (puedes instalarlo con `pip install jupyter-book`)

### Pasos para Construir y Visualizar el Libro:

1.  **Navega al directorio raíz de tu proyecto JupyterBook** en tu terminal:

    ```bash
    cd C:\Users\pc-57\Desktop\Code\50_Math_JupyterBook\MathBook
    ```

2.  **Asegúrate de que el contenido de los capítulos esté en su lugar**:
    Los archivos Markdown de tus capítulos (ej. `00_Introduction.md`, `01_Zero.md`) deben estar ubicados directamente en el directorio `chapters_content/` dentro de la raíz de tu JupyterBook. Si no lo están, cópialos desde `C:\Users\pc-57\Desktop\Code\50_Math\data\chapters_long` y renómbralos adecuadamente.

3.  **Verifica la configuración de `_config.yml` y `_toc.yml`**:
    Estos archivos ya deberían estar configurados con el título del libro, el autor, la habilitación de la ejecución de código y la lista de todos tus capítulos. Puedes abrirlos con un editor de texto para confirmar su contenido y la indentación.

4.  **Limpia la caché de construcción (opcional, pero recomendado si hay problemas)**:

    ```bash
    C:\Users\pc-57\AppData\Local\Programs\Python\Python313\Scripts\jupyter-book.exe clean .
    ```

5.  **Construye el libro**:

    ```bash
    C:\Users\pc-57\AppData\Local\Programs\Python\Python313\Scripts\jupyter-book.exe build .
    ```

6.  **Visualiza el libro**:
    Una vez que la construcción se complete, el libro web estático se generará en el directorio `_build/html/`. Abre el archivo `index.html` en tu navegador para ver el libro:

    ```bash
    start _build\html\index.html
    ```

## Organización de Carpetas y Archivos:

Ahora que el proyecto ha migrado a JupyterBook, la estructura ideal de carpetas es la siguiente:

```
C:\Users\pc-57\Desktop\Code\
├── 50_Math_JupyterBook/       # Este es tu nuevo proyecto principal
│   └── MathBook/              # La raíz de tu libro JupyterBook
│       ├── _build/            # Contiene el sitio web estático generado
│       ├── _config.yml        # Configuración del libro
│       ├── _toc.yml           # Tabla de contenidos del libro
│       ├── intro.md           # Página de introducción del libro
│       ├── chapters_content/  # **Aquí es donde residen todos tus archivos de capítulo (.md)**
│       │   ├── 00_Introduction.md
│       │   ├── 01_Zero.md
│       │   ├── ...
│       │   └── 51_Glossary.md
│       ├── GEMINI.md          # Documentación del proyecto original (copia)
│       └── README.md          # README del proyecto original (copia)
│
└── 50_Math/                   # Tu proyecto Flask original (ahora redundante)
    ├── data/
    │   ├── chapters/
    │   └── chapters_long/
    │   └── ...
    ├── math_app/
    │   └── ...
    └── ...
```

### Qué se puede eliminar:

Una vez que estés completamente satisfecho con el funcionamiento de tu JupyterBook y hayas verificado que todo el contenido y la interactividad están presentes, puedes considerar eliminar el proyecto Flask original para evitar duplicidades y mantener tu espacio de trabajo limpio.

**Proyecto Flask Original (`C:\Users\pc-57\Desktop\Code\50_Math`)**: Puedes eliminar esta carpeta completa. Contiene la aplicación Flask, los datos originales y los archivos de configuración que ya no son necesarios para el JupyterBook.

**ADVERTENCIA**: Antes de eliminar, asegúrate de hacer una copia de seguridad de `C:\Users\pc-57\Desktop\Code\50_Math` si crees que podrías necesitar algo de allí en el futuro. La eliminación es irreversible.