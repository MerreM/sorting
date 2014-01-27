import random

def bubble_sort(seq):
    """Inefficiently sort the mutable sequence (list) in place.
    seq MUST BE A MUTABLE SEQUENCE.

    As with list.sort() and random.shuffle this does NOT return 
    """
    changed = True
    while changed:
        changed = False
        for i in xrange(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return None

sort_me = [random.randint(0,100) for x in range(0,100)]

print "Before %s\n"%sort_me
#
bubble_sort(sort_me)

print "After %s\n"%sort_me

