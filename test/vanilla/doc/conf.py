# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Vanilla Autorest doc'
copyright = '2020, Autorest Python team'
author = 'Autorest Python team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'sphinx.ext.doctest',
              'sphinx.ext.viewcode', 'sphinx.ext.intersphinx', 'sphinx.ext.napoleon',
              'sphinx_rtd_theme'
]

intersphinx_mapping = {
    # Dependencies
    'python': ('https://docs.python.org/3.8', None),
    # 'msrestazure': ('http://msrestazure.readthedocs.io/en/latest/', None),
    # 'msrest': ('http://msrest.readthedocs.io/en/latest/', None),
    'requests': ('https://requests.kennethreitz.org/en/master/', None),
    'aiohttp': ('https://aiohttp.readthedocs.io/en/stable/', None),
    'trio': ('https://trio.readthedocs.io/en/stable/', None),
    'msal': ('https://msal-python.readthedocs.io/en/latest/', None),
    # Azure packages
    'azure-core': ('https://azuresdkdocs.blob.core.windows.net/$web/python/azure-core/1.1.1/', None),
    'azure-identity': ('https://azuresdkdocs.blob.core.windows.net/$web/python/azure-identity/1.1.0/', None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']