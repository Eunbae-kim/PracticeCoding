# python
# returns a first list of all the keys in a flat dictionary
def allKeys(dictionary):
    return list(dictionary.keys())


grades = {
    'SooJung' : 100,
    'Minsu' : 78,
    'Ayoung' : 87,
    'Chulsoo' : 57,
}

print(allKeys(grades), type(allKeys(grades))) #['SooJung', 'Minsu', 'Ayoung', 'Chulsoo'] <class 'list'>
