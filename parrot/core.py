#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals
)


class DataObj:

    def __init__(self, str, *args, **kwargs):
        self.docs = None
        self.span = None
        str = self.preprocess(str)

    def preprocess(self, str):
        return str


class IdentifierBase:
    def __init__(self, model, *args, **kwargs):
        self.model = model

    def predict_proba(self):
        raise NotImplementedError

    def decision_fn(self):
        raise NotImplementedError

    def __call__(self):
        raise NotImplementedError


class RuleBase:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def apply(self, x):
        raise NotImplementedError

    def __call__(self, x):
        return self.apply(x)


class Sequential:
    def __init__(self, rule_list):
        assert len(rule_list) > 0
        assert issubclass(type(rule_list[0]), RuleBase)
        self.rules = rule_list
        super(Sequential, self).__init__()

    def __call__(self, x):
        for rule in self.rules:
            x = rule(x)