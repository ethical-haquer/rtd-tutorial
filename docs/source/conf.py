# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Galaxy Flasher'
copyright = '2024, ethical_haquer'
author = 'ethical_haquer'

release = ''
version = ''

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx.ext.autosectionlabel',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

nitpicky = True

autosectionlabel_prefix_document = True

copybutton_prompt_text = "$ "

# -- Options for HTML output

html_theme = "furo"

html_theme_options = {
    "announcement": "<em>Notice:</em> These docs are still under development.",
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
