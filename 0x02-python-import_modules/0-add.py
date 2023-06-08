#!/usr/bin/env python3
if __name__ == "__main__":
    import add_0.add
    a = 1
    b = 2
    print("{one:d} + {two:d} = {result:d}".format(one=a,
                                                  two=b, result=add(a, b)))
