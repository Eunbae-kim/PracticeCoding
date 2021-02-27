# python
# list comprehension
# Returns a list of elements that exist in both lits.

#Using list comprehension on a to only keep value containe din both lists.
def listInBothList(a,b):
    return [item for item in a if item in b] # we go over all elements in a and make a list if it is also in b

a = [1,2,3,4,5,6]
b = [1,2,5,7,8,11]
print(listInBothList(a,b))
