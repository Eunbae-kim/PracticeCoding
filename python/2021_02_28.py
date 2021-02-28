# python
# Splits a multiline string into a list of lines.

# we can use split('\n')
def splitLinesToList(lines):
    return lines.split('\n')

# or we can use splitlines function in string
def splitLinesToList2(lines):
    return lines.splitlines()

lines = 'This\nis \na \nlines'

print(lines, type(lines))
print(splitLinesToList(lines), type(splitLinesToList(lines)))
print(splitLinesToList2(lines), type(splitLinesToList2(lines)))
