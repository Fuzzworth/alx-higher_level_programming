#!/usr/bin/python3
import importlib.util
spec = importlib.util.spec_from_file_location("hidden", "./hidden_4.pyc")
hidden_m = importlib.util.module_from_spec(spec)
modules = dir()
if __name__ == "__main__":
    for module in modules:
        if (not module.startswith("__")):
            print(module)
