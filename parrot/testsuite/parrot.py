#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `parrot` module."""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals
)

from .. import core

from . import unittest


class ParrotTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def test_something_docstring(self):
        """Here is a sample test with a docstring. Hey."""
        self.assertTrue(True)

    def tearDown(self):
        pass


def suite():
    from .helpers import setup_path
    setup_path()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ParrotTestCase))
    return suite
