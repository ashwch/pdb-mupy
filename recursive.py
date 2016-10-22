# -*- coding: utf-8 -*-
import pdb


def func(n):
    if n > 0:
        return func(n - 1)
    else:
        pdb.set_trace()
        return 0


if __name__ == '__main__':
    print (func(4))
