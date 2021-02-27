#python
# returns true if the given number is even, false otherwise

def isEven(a): # we can shorten the code to ' return num %2 == 0 '
    if(a%2 == 0):
        return True
    else:
        return False

print("Is 3 even? ", isEven(3))
print("Is 24 even? ", isEven(24))
