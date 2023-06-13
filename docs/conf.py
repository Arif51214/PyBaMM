# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import pybamm

sys.path.insert(0, os.path.abspath("../"))


# -- Project information -----------------------------------------------------

project = "PyBaMM"
copyright = "2018-2023, The PyBaMM Team"
author = "The PyBaMM Team"

# The short X.Y version
version = pybamm.__version__
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_extend_parent",
    "sphinx_inline_tabs",
    "sphinxcontrib.bibtex",
]

# -- sphinxcontrib-bibtex configuration --------------------------------------
bibtex_bibfiles = ["../pybamm/CITATIONS.bib"]
bibtex_style = "unsrt"
bibtex_footbibliography_header = "References"


napoleon_use_rtype = True
napoleon_google_docstring = False

doctest_global_setup = """
from docs import *
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# Suppress warnings generated if footnotes are not references in a docstring
suppress_warnings = ["ref.footnote"]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_static_path = ["source/_static"]

# Theme

# pydata theme options (see
# https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html# for more information)
# mostly copied from numpy, scipy, pandas
html_logo = "source/_static/pybamm_logo.png"
html_favicon = "source/_static/favicon/favicon.png"

html_theme_options = {
    "logo": {
        "image_light": "pybamm_logo.png",
        "image_dark": "pybamm_logo.png",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pybamm-team/pybamm",
            "icon": "fa-brands fa-square-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/pybamm_",
            "icon": "fa-brands fa-square-twitter",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/pybamm/",
            "icon": "fa-solid fa-box",
        },
    ],
    "collapse_navigation": True,
    "external_links": [
        {
            "name": "Examples",
            "url": "https://github.com/pybamm-team/PyBaMM/tree/develop/examples",
        },
        {
            "name": "Contributing",
            "url": "https://github.com/pybamm-team/PyBaMM/tree/develop/CONTRIBUTING.md",
        },
    ],
    "switcher": {
        "version_match": release,
        "json_url": "https://pybamm.readthedocs.io/en/latest/_static/versions.json",  # noqa: E501
    },
    # turn to False to not fail build if json_url is not found
    "check_switcher": True,
    # for dark mode toggle, version switcher, and social media links
    "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
    "use_edit_page_button": True,
}

html_title = "%s v%s Manual" % (project, version)
html_last_updated_fmt = "%b %d, %Y"
html_css_files = ["pybamm.css"]
html_context = {"default_mode": "light"}
html_use_modindex = True
html_copy_source = False
html_domain_indices = False
html_file_suffix = ".html"

htmlhelp_basename = "pybamm"

html_sidebars = {"**": ["sidebar-nav-bs.html", "sidebar-ethical-ads.html"]}

# For edit button
html_context = {
    "github_user": "pybamm-team",
    "github_repo": "pybamm",
    "github_version": "develop",
    "doc_path": "docs/",
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "PyBaMMdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, "PyBaMM.tex", "PyBaMM Documentation", author, "manual")]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "pybamm", "PyBaMM Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "PyBaMM",
        "PyBaMM Documentation",
        author,
        "PyBaMM",
        "One line description of project.",
        "Miscellaneous",
    )
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "matplotlib": ("https://matplotlib.org", None),
}

# -- Jinja templating --------------------------------------------------------
# Credit to: https://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/


def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != "html":
        return
    src = source[0]
    rendered = app.builder.templates.render_string(src, app.config.html_context)
    source[0] = rendered


def setup(app):
    app.connect("source-read", rstjinja)


# Context for Jinja Templates
html_context.update(
    {
        "parameter_sets": pybamm.parameter_sets,
    }
)
