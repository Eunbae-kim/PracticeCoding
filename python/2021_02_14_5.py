# python
# Returns True if there are duplicate values in a flat list, False otherwise.
from collections import Counter

def IsDuplcate(list):
    count_values = Counter(list)
    print(count_values)
    for i,z in count_values.items():
        if z>1:
            return True
    return False

x = [1,2,3,4,4,5,6,7]
y = [1,2,3,4,5,6,7]

print("Are there duplicate values in x?", IsDuplcate(x))
print("Are there duplicate values in y?", IsDuplcate(y))


## or simply we can use set()
def IsDuplcate(list):
    return len(list) != len(set(list))

x = [1,2,3,4,4,5,6,7]
y = [1,2,3,4,5,6,7]

print("Are there duplicate values in x?", IsDuplcate(x))
print("Are there duplicate values in y?", IsDuplcate(y))
