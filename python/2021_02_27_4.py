#python
# Returns a random elemnt from a list.
# Returns N randoms elemnt from a list.

from random import randint
from random import sample

def randomOne(list):
    return list[randint(0,len(list)-1)] #randiant is the method which return one random int from 0 to len(list)-1 in the list

def randomN(list,n):
    return sample(list, n)

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(randomOne(a)) #return random value
print(randomN(a,3)) #return N random value
