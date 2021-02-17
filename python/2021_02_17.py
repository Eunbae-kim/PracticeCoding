# python
# returns the most frequent element in a list.
def mostFrequent(list):
    return max(set(list), key=list.count) #입력 된 리스트에서 개수가 가장 많은 값 returns

list = [1,2,3,1,2,1]
print(mostFrequent(list))



"""
Using max & set functions :
create a set of the list for deleting the duplicate values -> set()
make use of max() which takes in two arguments an iterable
        & a key function which will return mostly occurred value
"""
