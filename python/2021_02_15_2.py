# python
# Returns all the elemetns of a list except the last one.
def allExceptLast(list):
    return(list[0:len(list)-1])

list = [1,2,3,4,5,6,8]
print(allExceptLast(list))
print(len(list) - 1)
