# Return True if all the values in a list are unique, False other wise.
list1 = [1,2,3,4,5]
list2 = [1,2,2,3,4]


def isUnique(list):
    if len(list) == len(set(list)):
            return True;
    else:
            return False;

if isUnique(list1):
    print("all the values in a list are unieqe")
else:
    print("There are same values in a list")

if isUnique(list2):
    print("all the values in a list are unieqe")
else:
    print("There are same values in a list")
