# -*- coding: utf-8 -*-
"""
Policy Studio Package.

This sub-package contains the tools for defining, validating (linting),
and compiling the ethical policies that govern the Shofar ecosystem.
"""
from .ethics_linter import EthicsLinter
from .compiler import PolicyCompiler

print("Policy Studio package initialized.")
