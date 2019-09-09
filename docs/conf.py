import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__name__))+"/../sklite")

project = 'SkLite'
copyright = '2019, Alexander Ejbekov'
author = 'Alexander Ejbekov'

release = '0.0.1'

extensions = [
    'sphinx.ext.autodoc',
    'numpydoc',
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'

html_static_path = ['_static']

numpydoc_show_class_members = False
numpydoc_show_inherited_class_members = False
numpydoc_use_blockquotes = False
master_doc = 'index'
