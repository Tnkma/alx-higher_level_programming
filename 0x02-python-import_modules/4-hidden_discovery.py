#!/usr/bin/python3
import importlib

mod = importlib.import_module("hidden_4")
for name in dir(mod):
    if not (name.startswith('__') and name.endswith('__')):
        print(name)
