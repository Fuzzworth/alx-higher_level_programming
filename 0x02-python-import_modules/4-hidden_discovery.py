#!/usr/bin/python3
modules = dir(__import__.('hidden_4'))
if __name__ == "__main__":
    for module in modules:
        if (not module.startswith("__")):
            print(module)
