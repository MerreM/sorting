import random
 
def bogosort(l):
    while not in_order(l):
        random.shuffle(l)
    return l
 
def in_order(l):
    if not l:
        return True
    last = l[0]
    for x in l[1:]:
        if x < last:
            return False
        last = x
    return True

def main():
    sort_me = [random.randint(0,100) for x in range(0,100)]

    print "Before %s\n"%sort_me
    #
    bogosort(sort_me)

    print "After %s\n"%sort_me

if __name__=="__main__":
    main()