##### Configuration file for the Sphinx documentation builder.

import os, sys
import sphinx_rtd_theme

# sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../surveyweathertool/src/"))
# sys.path.insert(0, os.path.abspath("../surveyweathertool/src"))

extensions = [
    # "sphinxcontrib.apidoc",
    "autoapi.extension",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",  # todo support
    # "sphinx.ext.autodoc",  # Core library for html generation from docstrings
    # "sphinx.ext.autosummary",  # Creatse neat summary tables
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

autoapi_dirs = ["../surveyweathertool/src/"]

# -- Options for apidoc extension --------------------------------------------
# see options here https://github.com/sphinx-contrib/apidoc
# apidoc_module_dir = "../surveyweathertool/src/"
# apidoc_module_first = True

# -- Options for autosummary extension --------------------------------------------

# make docs automatically
# autosummary_generate = True  # Turn on sphinx.ext.autosummary


# # Autodoc settings
# autodoc_member_order = "bysource"  # Order members by their source order
# autodoc_default_flags = ["members", "undoc-members", "private-members"]

# # Add modules to be included in the documentation
# autodoc_mock_imports = [
#     "survey",
#     "weather",
#     "weather_x_survey",
# ]  # If you need to mock certain imports

# # Add the path to the module(s) you want to document
# # For example, if you have a module named 'my_module' to document:
# autodoc_modules = ["weather"]

# Optionally, configure the file patterns for which to generate documentation
# For example, to include all Python files in a specific directory:
# exclude_patterns = ['_build', '**/tests', '**/venv']


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
##### TODO: Still to edit and add as required by Jumpstart team

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
# html_theme = "default"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

man_pages = [
    ("index", "stc_unicef_cpi", "stc_unicef_cpi Documentation", ["DSSG-STC-UNICEF"], 1)
]

# Output file base name for HTML help builder.
# htmlhelp_basename = "jmpst"

# -- Options for EPUB output

epub_show_urls = "footnote"
copyright = "2023 Data Science for Social Good (RPTU and DFKI)"

author = (
    "Trey Roark, Prahitha Movva, Moshood Yekini, Shikhar Mishra, Jama Hussein Mohamud"
)

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# TODO support
todo_include_todos = False
todo_emit_warnings = True

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "jumpstart"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "0.1"
# The full version, including alpha/beta/rc tags.
release = "0.1.0"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".gitignore"]
