#python
# There is one ATM.
# There are N people infront of the ATM
# The sum of the time to get the money depends on the order in which people line up.

n = int(input())
list = list(map(int, input().split()))

def minTime(n, list):
    list.sort() # The return value of sort() : None
    sum = 0
    for i in range(n):
        for j in range(i+1):
           sum += list[j]
    print(sum)

minTime(n, list)
