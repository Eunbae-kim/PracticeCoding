# python
# Initializes a list containing the numbers in the specified range
# where start and end are inclusive with their common difference step.

def initializeList(end, start = 0, step = 1):
    return list(range(start, end + 1, step))

print(initializeList(7)) #[0, 1, 2, 3, 4, 5, 6, 7]
print(initializeList(7,3)) #[3, 4, 5, 6, 7]
print(initializeList(7,3,2)) #[3, 5, 7]
