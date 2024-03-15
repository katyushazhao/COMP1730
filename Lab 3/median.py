from random import shuffle

def is_sorted(l):
    '''Determine whether the list is sorted'''
    if l[0] <= l[1] and l[1] <= l[2]:
        return True
    else:
        return False

def median(a,b,c):
    '''Print median of a 3 item list'''
    l = [a,b,c]
    while not is_sorted(l):
        shuffle(l)
    print(l[1])
