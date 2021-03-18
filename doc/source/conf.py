# Configuration file for the Sphinx documentation builder.

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'python-devicetree'

# Placeholders based on initial provenance of the documentation.
copyright = u'2021 Zephyr Project members and individual contributors'
author = 'Zephyr Project'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    # Keep this sorted; don't just append new items.
]

templates_path = ['_templates']

exclude_patterns = []

rst_epilog = f'''
.. |release| replace:: {release}
'''

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = []
