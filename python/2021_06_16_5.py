# python
# returns the n maximun elements from the provided list.

def nMaxValue(list, n):
    list.sort()
    return list[len(list)-n:]

print(nMaxValue([1,2,3,4,5,6],1))
print(nMaxValue([1,2,3,4,5,6],2))
print(nMaxValue([1,2,3,6,7,8,6],5))


# in other wyas
# we can use sorted() to sort the list
# and the to get the specified number, [:n]
# return sorted(list, reverse = True)[:n]
