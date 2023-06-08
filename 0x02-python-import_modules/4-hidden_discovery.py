#!/usr/bin/python3
import importlib.util

module_name = 'hidden_4'  # Replace with your .pyc module name (without the extension)
module_path = './hidden_4.pyc'  # Replace with the actual path to your .pyc file

spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Use dir() to get the attributes and methods of the module
module_attributes = dir(module)

# Filter and print only the lines that don't start with "__"
filtered_attributes = [attr for attr in module_attributes if not attr.startswith('__')]
for attribute in filtered_attributes:
    print(attribute)
