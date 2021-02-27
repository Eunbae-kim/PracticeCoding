# python
# Check if the first numeric argument is divisible by the second one.

def isDivisible(a,b):
    if((a%b) == 0):
        return True
    return False

print(" if the 12 is divisible by 3 ?  ", isDivisible(12,3))
print(" if the 12 is divisible by 5 ?  ", isDivisible(12,5))
