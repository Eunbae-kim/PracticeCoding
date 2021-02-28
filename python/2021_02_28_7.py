# python
# Returns a flat list of all the values in a flat dictionary

# we can use values() funciton to get all values in dictionary
# then using list() function, we can make it as a list

def valuesList(dictionary):
    return list(dictionary.values())

ages = {
    "eunbae":100,
    "soojeong":103,
    "yea":99,
}

print(valuesList(ages))
