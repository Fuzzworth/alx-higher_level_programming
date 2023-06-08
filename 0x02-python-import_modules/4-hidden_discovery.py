#!/usr/bin/python3
import hidden_4
modules = dir()
if __name__ == "__main__":
    for module in modules:
        if (!module.statswith("__")):
            print(module)
