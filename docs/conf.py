import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'ADCTP2'
author = 'Dinis Pedrosa, Diogo Lameirão, Rafael Pereira, Alexandre Formozinho'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
]

autosummary_generate = True
autosummary_imported_members = True

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
