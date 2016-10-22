# -*- coding: utf-8 -*-
import sys


def divide(numerator, denominator):
    #  To set a breakpoint at the start of this function use `break divide`
    #  To set a breakpoint on divide only when denominator == 0: break divide, denominator == 0
    print "Calculating {}/{}".format(numerator, denominator)
    return numerator / denominator  #  To set a breakpoint on this line use `break 9`


if __name__ == '__main__':
    numerator = float(sys.argv[1])
    denominator = float(sys.argv[2])
    print divide(numerator, denominator)
