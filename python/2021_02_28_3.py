# phthon
# Returns all elemetns in a list except for the first one.

def exceptFirstOne(list):
    if len(list) >1:
        return list[1:]
    else:
        return list

#or simply, we can code : return list[1:] if len(list) > 1 else list

print(exceptFirstOne([1,2,3,4]))
print(exceptFirstOne([1]))
