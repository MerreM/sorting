import random

def quicksort(in_list):
    if len(in_list) <= 1:
        return in_list  # an in_list of zero or one elements is already sorted
    less = []
    more = []
    pivot = random.choice(in_list)
    in_list.remove(pivot)
    for x in in_list:
        if x <= pivot:
            less.append(x)
        else:
            more.append(x)
    return quicksort(less)+[pivot]+quicksort(more) # two recursive calls


def main():
    sort_me = [random.randint(0,100) for x in range(0,100)]

    print "Before %s\n"%sort_me
    #
    quicksort(sort_me)

    print "After %s\n"%sort_me

if __name__=="__main__":
    main()