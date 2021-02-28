# python
# Returns a list with n elements removed from the end

# set the initial value of the n to 1. (If people do not specify the n, then we return only the list one)

def takeNFromBack(list, n = 1):
    return list[-n:] #if we write -, than it return from backwards

print(takeNFromBack([1,2,3,4,5],4))
print(takeNFromBack([1,2,3,4,5]))
