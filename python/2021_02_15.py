# python
# Check if the given number falls within the given range.

def withinRange(n, start, end):
    if n >= start and n <=end:
        return True
    else:
        return False



print(withinRange(6,2,12))
print(withinRange(1,2,12))
