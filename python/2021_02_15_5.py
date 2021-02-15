# python
# Returns a lsit of elements that exist in both lists.

def elemnetsExitInBoth(list1, list2):
    list = []
    for i in list1:
        for z in list2:
            if i == z:
                list.append(z)
    return list

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,2]

print(elemnetsExitInBoth(list1, list2))

# other way
#def elemnetsExitInBoth(list1, list2):
#    _a, _b = set(list1), set(list2)    # make both list to sets
#    return list(_a & _ b)              # using &, we can have intersaction of both sets.
