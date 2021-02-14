# python
# Filter out the non-unique values in a list
# Use collections.Counter : dic subclass for counting hashtable objects.


from collections import Counter

def filterNonUnique(list):
    count_values = Counter(list)
    print(count_values)
    for i,z in count_values.items():
        #print(i)
        #print(z)
        if z==1:
            print(i)

filterNonUnique([1,2,2,3,4,4,5])
