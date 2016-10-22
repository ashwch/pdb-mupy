import pdb


def mupy(foo, bar):
    print "MUPy started"
    var = 100
    if foo:
        print "foo is true"
    else:
        print "foo is false"

    if "horse" in bar:
        print "A horse walked into a bar"
    else:
        print var
    return None


pdb.set_trace()
mupy(foo=True, bar="horse")
