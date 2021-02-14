# python
# Executes the provided function once for each list element

def executesFuncEach(list, function):
    for i in list: # using for, excutes the function to each element.
        function(i)

# test
executesFuncEach([1,2,3,4,5,6],print)
