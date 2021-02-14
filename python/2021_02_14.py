# python
# Return every nth element in a list

def everyNth(list, n):
    return list[n-1::n]

#test
# [3, 6, 9] 리턴
print(everyNth([1,2,3,4,5,6,7,8,9],3))
