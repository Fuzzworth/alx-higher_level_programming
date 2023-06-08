#!/usr/bin/python3
import importlib.util

module_name = 'hidden_4'
module_path = './hidden_4.pyc'

spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

names = [name for name in dir(module) if not name.startswith('__')]
names.sort()

for name in names:
    print(name)

