#Python For Loops
"""A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc."""

fruits = ["apple","banana","kiwi","orange"]
for x in fruits:
    print(x)
    #The for loop does not require an indexing variable to set beforehand.

#>>>>>>>>>>>>>>>>>>>>>>>>
#1  Looping Through a String: Even strings are iterable objects, they contain a sequence of characters:

name = "Manoj Reddy"
for x in name:
    print(x)

#>>>>>>>>>>>>>>>>>
#2  The break Statement :With the break statement we can stop the loop before it has looped through all the items:

fruits1 = ["apple","banana","kiwi","orange"]
for x in fruits1:
    print(x)
    if x == "banana":
        break


#Exit the loop when x is "banana", but this time the break comes before the print:
fruits2 = ["apple","banana","kiwi","orange"]
for x in fruits2:
    if x == "banana":
        break
    print(x)



#>>>>>>>>>>>>>

#3  The continue Statement: With the continue statement we can stop the current iteration of the loop, and continue with the next:

fruits3 = ["banana","orange","apple","kiwi","mango"]
for x in fruits3:
   
    if x == "orange":
        continue
    print(x)


    #The range() Function:
"""To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number."""
for x in range(6): #range from 0 to 5
    print(x)

for x in range(2,6): # range from 2 to 5
    print(x)

for x in range(2,30,3):# range from 2 to 30 by adding 3 for every element
    print(x)

#>>>>>>>>>>>>>>>>>>>>
# Else in For Loop:The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
    print(x)
else:
    print("the loop has been finished")

    #Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("nothig")

#>>>>>>>>>>>>>>>>>>>>>>>>>
#Nested Loops:

"""A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":"""

color = ["red","greean","orange","yellow","pink"]
fruits = ["banana","apple","orange","kiwi","mango"]
for x in color:
    for y in fruits:
        print(x,y)

#pass statement
"""for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error."""
for x in [0,1,3]:
    pass