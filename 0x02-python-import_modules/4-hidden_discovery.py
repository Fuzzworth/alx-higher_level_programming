#!/usr/bin/python3
import importlib.util
module_name = 'hidden_4'  # Replace with your .pyc module name (without the extension)
module_path = './hidden_4.pyc'  # Replace with the actual path to your .pyc file
spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
modules = dir(module_name)
if __name__ == "__main__":
    for m in modules:
        print(m)
