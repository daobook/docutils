# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# #
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from pathlib import Path


# -- Project information -----------------------------------------------------

project = 'docutilsx'
copyright = '2021, xinetzone'
author = 'xinetzone'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxext.rediraffe',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    'docutils/test', 'docutils/docutils',
                    'docutils/tools/**', 'docutils/licenses/**',
                    # 'docutils/docs/user/rst/quickref.html',
                    # 'docutils/docs/user/rst/demo.txt',
                    'requirements.txt', 'prest/**']

exclude_patterns += [p.as_posix() for p in Path('sandbox').iterdir() if p.is_dir()]
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
}

locale_dirs = ['locales/']  # path is example but recommended.
gettext_compact = False  # optional.
html_favicon = "favicon.png"

rediraffe_redirects = {
    "web/README": "docutils/README",
    "web/docs/index": "docutils/docs/index",
    "web/docs/user/mailing-lists": "docutils/docs/user/mailing-lists",
    "web/BUGS": "docutils/BUGS",
    "web/docs/dev/todo": "docutils/docs/dev/todo",
    "web/RELEASE-NOTES": "docutils/RELEASE-NOTES",
    "web/docs/dev/repository": "docutils/docs/dev/repository",
    "web/sandbox/README": "sandbox/README",
}

