# python
# Returns a list of elements that exist in both lists.

def returnIntersection(a,b):
    _a, _b = set(a), set(b) # we can create a set from a and b
    return list(_a & _b)  # use & to only keep values contained in both sets.

def returnIntersection2(a,b):
    _a, _b = set(a), set(b) # we can create a set from a and b
    return list(_a.intersection(_b))  #or we can use intersection methond in set

a = [1,2,3,4,5]
b = [4,5,6,7,8]
print(returnIntersection2(a,b))
