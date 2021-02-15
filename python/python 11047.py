# python
# There are N types of coins,
# and there are many of each coin.

# we wanna make the value of coins into sum K.
# How can we have the minimun number of coins?
def minCoins(n, k,values):
    value = k
    count = 0
    i = len(values) - 1

    for z in range(n):
        if((value // values[i]) >= 1):
            print(value)
            print(values[i])
            print('yes')
            count += value // values[i]
            value = value - values[i]*(value // values[i])
            print(count)
        i -= 1
    return count

n,k = list(map(int, input().split()))
values = []
for i in range(n):
    a = int(input())
    values.append(a)

print(minCoins(n,k,values))
