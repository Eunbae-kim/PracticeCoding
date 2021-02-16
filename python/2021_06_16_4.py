# python
# Returns the index of the element with the maximun value in a list

def maximun(list):
    max = list[0]
    maxindex = 0
    for i,z in enumerate(list):
        if( max < z):
            max = z
            maxindex = i
    return maxindex


list =[4,6,2,7,4,65,7]
print(maximun(list))#5

# OR in other ways,
# we can use max() to find out the miaximun value in the list
# and we can use list.index() to get the index
# return list.index(max(list))
