#!/usr/bin/python3
import importlib.util
module_name = 'hidden'  # Replace with your .pyc module name (without the extension)
module_path = './hidden_4.pyc'  # Replace with the actual path to your .pyc file
spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
modules = dir("hidden")
if __name__ == "__main__":
    for m in modules:
        if (not m.startswith("__")):
            print(m)
