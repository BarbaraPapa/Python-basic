# Exercise 1  string data type
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))


# Exercise 2  string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


#Exercise 3  input strings
name = input("What is your name? ")
print(name)


# Exercise 4  Formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
