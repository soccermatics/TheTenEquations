# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_gallery
from sphinx_gallery.sorting import ExplicitOrder
from sphinx_gallery.sorting import ExampleTitleSortKey

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Ten Equations'
copyright = '2022, David Sumpter'
author = 'David Sumpter'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.mathjax',
              'sphinx_gallery.gen_gallery',
              'sphinxcontrib.youtube',
              'myst_parser'
              ]

templates_path = ['_templates']
exclude_patterns = []


# sphinx gallery
sphinx_gallery_conf = {
    'examples_dirs': ['../lessons'],
    'gallery_dirs': ['gallery'],
	'image_scrapers': ('matplotlib'),
    'matplotlib_animations': True,
	'within_subsection_order': ExampleTitleSortKey,
    'subsection_order': ExplicitOrder(['../lessons/lesson1',
                                       '../lessons/lesson2',
                                       ])}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_show_sourcelink = False
html_show_contentslink = False

def setup (app):
    app.add_css_file('css/custom.css')


# add logo
html_logo = "images/TENLogo.png"
html_theme_options = {'logo_only': True,
                      'display_version': False}
