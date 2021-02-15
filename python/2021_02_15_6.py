# python
# Checks if the first numeric argumetn is divisible by the second one.

def isDivisible(divided, divisor):
    if divided % divisor == 0:
        return True
    else:
        return False

print(isDivisible(8,2)) # True
print(isDivisible(8,3)) # False
