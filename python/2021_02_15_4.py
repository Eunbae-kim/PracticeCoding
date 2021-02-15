# python
# Initializes and fills a list with the specified value.

def initializeWithSpecified(n, value):
    list = []
    for i in range(n):
        list.append(value)
    return list

print(initializeWithSpecified(10,6))

# other way
# return [value for x in range(n)]
