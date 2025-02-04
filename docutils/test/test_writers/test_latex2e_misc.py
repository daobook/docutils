#! /usr/bin/env python
# coding: utf-8

# $Id$
# Author: Günter Milde
# Maintainer: docutils-develop@lists.sourceforge.net
# :Copyright: 2020 Günter Milde,
# :License: Released under the terms of the `2-Clause BSD license`_, in short:
#
#    Copying and distribution of this file, with or without modification,
#    are permitted in any medium without royalty provided the copyright
#    notice and this notice are preserved.
#    This file is offered as-is, without any warranty.
#
# .. _2-Clause BSD license: https://opensource.org/licenses/BSD-2-Clause

"""
Miscellaneous LaTeX writer tests.
"""
from __future__ import absolute_import
import warnings

if __name__ == '__main__':
    import __init__
from test_writers import DocutilsTestSupport
from docutils import core

contents_test_input = """\
.. contents:: TOC

foo
---

bar
---

"""

class TocTestCase(DocutilsTestSupport.StandardTestCase):

    def test_publish_from_doctree(self):
        """Ignore the Docutils-generated ToC, when ``use_latex_toc``
        is True. (This did happen when publishing from a doctree.)
        """
        mysettings = {'output_encoding': 'unicode',
                      '_disable_config': True,
                      # avoid latex writer future warnings:
                      'use_latex_citations': False,
                      'legacy_column_widths': True,
                     }
        doctree = core.publish_doctree(contents_test_input,
                                       settings_overrides=mysettings)
        result = core.publish_from_doctree(doctree,
                                     writer_name='latex',
                                     settings_overrides=mysettings)
        self.assertNotIn(r'\item \hyperref[foo]{foo}', result)
        # self.assertIn(r'\tableofcontents', result)


class WarningsTestCase(DocutilsTestSupport.StandardTestCase):

    def test_future_warnings(self):
        """Warn about changing defaults."""
        mysettings={'_disable_config': True,
                    # 'use_latex_citations': False,
                    # 'legacy_column_widths': True,
                   }
        with warnings.catch_warnings(record=True) as wng:
            warnings.simplefilter("always")
            core.publish_string(u'warnings test', writer_name='latex',
                                settings_overrides=mysettings)
            self.assertEqual(len(wng), 2, "Expected 2 FutureWarnings.")
            assert issubclass(wng[0].category, FutureWarning)
            assert issubclass(wng[1].category, FutureWarning)


if __name__ == '__main__':
    import unittest
    unittest.main()
