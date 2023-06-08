#!/usr/bin/python3
import imp
hidden_module = = imp.load_compiled("hidden", "./hidden_4.pyc")
modules = dir()
if __name__ == "__main__":
    for module in modules:
        if (not module.startswith("__")):
            print(module)
