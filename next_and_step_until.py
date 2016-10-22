# -*- coding: utf-8 -*-
import pdb


def knights():
    print "We are the Knights who say ni!"
    # Done with this function. Want to reach the end this function? Use r(eturn).
    print "Get us a shrubbery."


def credits():
    print "A Møøse once bit my sister... No realli!"
    print "We apologise for the fault in the print statements."
    print "Those responsible have been sacked."
    return "Møøse bites Kan be pretti nasti."



pdb.set_trace()

knights()  # Just want to run this function and move on to next line? Use n(ext).
credits()  # Want to step inside this function? Use s(tep).

for i in range(1, 5):
    # To exit loop unt(il) can be used.
    print "Shrubbery #{}".format(i)

print "We have found the Holy Grail."
