# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Extruder Principles and Operations/中文版'
copyright = '2023, Bobolin'
author = 'Bobolin'

release = '1.0'
version = '1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_copybutton',
    "sphinx_design",
    'sphinx.ext.autosectionlabel',
    
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    #"linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output

epub_show_urls = 'footnote'


# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`

autosectionlabel_prefix_document = True

autosectionlabel_maxdepth = 1 

