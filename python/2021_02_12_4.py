# python
# Returns the difference between two interables

def difference (interable1, interable2):
    return list(set(interable1) - set(interable2))


a=[1,2,3,4]
b =[2,3,4]

print(difference(a,b))

# Using list conprehension
# def differecne(interable1, interable2):
#     interable = set(interable2)
#     return [out for out in interable1 if out not in interable]

# we can also use difference method in set
