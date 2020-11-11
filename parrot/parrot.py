#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals
)


class DataObj:

    def __init__(self, str):
        self.docs = None
        self.span = None
        str = self.preprocess(str)

    def preprocess(self, str):
        return str


