# python
# prints out the same string a defined number of times

def nTimesPrint(string, n):
    for i in range(n-1):
        string += string
    print(string)


string='love'
n = 2
nTimesPrint(string, n)

# or other way,
# we can just use multiply *
# return string*n
