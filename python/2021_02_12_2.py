# python
# Capitalizes the first letter of every word in a string

name = "kim_Eunbae"

#Using capitalize() function which capitalizes the first letter of every word in a string.
#We can have same result by using title() function.
def capitalizeFirstLetter(letter):
    print(letter.capitalize())

#Using upper() function which capitalies the letter and Slicing.
def upperFirstLetter(letter):
    print(letter[0].upper(), letter[1:])

capitalizeFirstLetter(name)
upperFirstLetter(name)
