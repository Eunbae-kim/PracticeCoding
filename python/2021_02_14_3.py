# python
# Filters out the unique values in a list

from collections import Counter

def FilterOutUnique(list):
    count_values = Counter(list)
    print(count_values)
    for i,z in count_values.items():
        #print(i)
        #print(z)
        if z>1:
            print(i)

FilterOutUnique([1,2,2,3,4,4,5])
