#
# Configuración de Documentación Sphinx para CSIC-ClimateWatch
#
import os
import sys
import importlib.metadata
from datetime import datetime

# Asegurar que src/ está en el path para la generación automática con autoapi
sys.path.insert(0, os.path.abspath("../src"))

current_year = datetime.now().year

# -- Información General del Proyecto -----------------------------------------
project = "CSIC-ClimateWatch"
copyright = f"Copyright © {current_year} Gustavo Liñán Cembrano y CSIC"
author = "Gustavo Liñán Cembrano"
html_show_sphinx = False

try:
    version = importlib.metadata.version("csic-climatewatch")
except importlib.metadata.PackageNotFoundError:
    version = "0.1.0"

# -- Configuración General -----------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "autoapi.extension",
]

# Configuración de AutoAPI para generar documentación automática desde docstrings
autoapi_type = "python"
autoapi_dirs = ["../src/csic_climate"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]

source_suffix = [".rst", ".md"]
master_doc = "index"
pygments_style = "default"
language = "es"

# -- Tema HTML -----------------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/guslicem/proyecto_final_curso_python_2026",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
    "show_toc_level": 2,
    "navbar_align": "left",
}

html_static_path = ["_static"]
