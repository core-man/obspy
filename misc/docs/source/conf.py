# -*- coding: utf-8 -*-
#
# ObsPy documentation configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#

import datetime
import glob
import obspy
import os
import sys

import matplotlib

import sphinx_rtd_theme


# Use matplotlib agg backend
matplotlib.use("agg")


# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
sys.path.append(os.path.abspath('_ext'))


# -- Project information -----------------------------------------------------
project = 'ObsPy'
author = 'The ObsPy Development Team (devs@obspy.org)'
year = datetime.date.today().year
copyright = '2012-{}, The ObsPy Development Team (devs@obspy.org)'.format(year)
version = ".".join(obspy.__version__.split(".")[:3])
release = obspy.__version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '3.1.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.duration',
    'sphinx.ext.todo',
    # theme
    'm2r',
    'sphinx_rtd_theme',
    # custom extensions
    'plot_directive',
    'credits',
    'citations',
]

# The file extensions of source files. Sphinx considers the files with this
# suffix as sources. The value can be a dictionary mapping file extensions to
# file types.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '_templates', '_ext']

# Warn about all references where the target cannot be found.
nitpicky = True
nitpick_ignore = ['norm_resp']

# configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'sqlalchemy': ('https://docs.sqlalchemy.org/en/latest/', None),
    'pip': ('https://pip.pypa.io/en/stable/', None),
}

# A boolean that decides whether module names are prepended to all object names
# (for object types where a “module” of some kind is defined).
add_module_names = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

html_logo = '_static/obspy_logo_no_text.svg'
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path 
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.min.css',
]

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {
}

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%dT%H:%M:%S'


# If true, a list all whose items consist of a single paragraph and/or a
# sub-list all whose items etc… (recursive definition) will not use the <p>
# element for any of its items.
html_compact_lists = True

# generate automatically stubs
autosummary_generate = glob.glob("packages" + os.sep + "*.rst")

# If true, autosummary already overwrites stub files by generated contents.
autosummary_generate_overwrite = False

# Don't merge __init__ method in auoclass content
autoclass_content = 'class'

# The default options for autodoc directives. They are applied to all autodoc
# directives automatically. It must be a dictionary which maps option names to
# the values.
# The supported options are 'members', 'member-order', 'undoc-members',
# 'private-members', 'special-members', 'inherited-members',
# 'show-inheritance', 'ignore-module-all', 'imported-members' and
# 'exclude-members'.
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'private-members': True,
    'special-members': True,
    'inherited-members': True,
}
