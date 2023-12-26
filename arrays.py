"""Note: python does not have built in arrays instead python will use list as arrays"""
#Arrays: here we acn see how list are used as arrays in python but we need to use NumPy library 

#Arrays are used to store multiple values in one single variable:

#creating arrays 

cars = ["volvo","benz","bmw"]

for x in cars: # looping through arrays
 print(x)

print(cars[0])# ACCESSING THE ELEMENT OF AN ARRAY
cars[0] = "roles"#CHANGING THE ELEMENT OF AN ARRAY
print(cars[0])
print(len(cars))# lenght of an array

cars.append("honda")#Add one more element to the cars array:
print(cars)

cars.remove("honda")#remove particular element
print(cars)

cars.pop(0)
print(cars)
#WHAT IS AN ARRAY: An array is a special variable, which can hold more than one value at a time.



#Array methods:
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.