# python
# Returns every element that exists in any of the two lists once.

# first we just sum two lists
# and we apply the set() function to delete duplicate elements
# and using list() function, we can make set type to list type
def union(list1, list2):
    return list(set(list1 + list2))



list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

print(list1 + list2) # Then we got duplicate elements too
print(type(set(list1+list2)))
print(union(list1, list2))
