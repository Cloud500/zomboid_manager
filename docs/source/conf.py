import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = 'Zomboid Server Manager'
copyright = 'Copyright (C) 2023, Licensed under the Apache License, Version 2.0'
author = 'Christian Heinisch <christian.heinisch@protonmail.com>'

extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.mermaid']

templates_path = ['_templates']
exclude_patterns = []
locale_dirs = ['locale/']
gettext_compact = False
language = 'en'
html_js_files = ['js/mermaid.js', ]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
