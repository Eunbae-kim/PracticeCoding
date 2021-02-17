# python
# Moves the specified amount of element to the end of the list

def moveValueToEnd(list, index):
    return list[index:] + list[:index] 


list = [0,1,2,3,4,5,6,7,8]
index =2
print(moveValueToEnd(list, index))
