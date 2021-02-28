# python
# Returns the sum of a list, after mapping each element to a value using the provided function


#input is dictionary
# we output the value which is the correct with the key given. (In this time, it is 'n')

def sumapplyFuction(list, function):
    return sum(map(function, list)) # we can use map() function to applay funciton to the each element of the list.

print(sumapplyFuction([{'n':4},{'n':12},{'n':5}], lambda v : v['n']))
