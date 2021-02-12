# python
# Counts the occurences of a value in a list

def countList(list, value):
    count = 0
    for i in list:
        if i == value:
            count += 1
    return count

list1 = [1,1,2,1,2,3,4,5,6,1]
print("There is " , countList(list1,1), " 1 in a list1")        
