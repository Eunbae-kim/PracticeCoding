# python
# Converts a number to a list of digits

def convertListOfDigits(num):
    res = [int(x) for x in str(num)]
    return res

a = 12345
print("Make ", a , "into a list of digits: ", convertListOfDigits(a))


# We can use map()
# def convertListOfDigits(num):
#     return list(map(int,str(num)))
