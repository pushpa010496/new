"""A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result."""

def my_fucntion():
    print("hello wolrd")
my_fucntion()

#1   Arguments: 
"""Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:"""

def name(fname):
    print(fname + " latha")
name("pushpa")
name("prema")
name("uha")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#2    number of arguments

"""By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less."""
def full_name(fname,lname):
    print(fname + ' ' + lname)
full_name("alishetti","pushpa")#If you try to call the function with 1 or 3 arguments, you will get an error:
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#3  Arbitrary Arguments, *args

def kids_names(*kids):
    print("The second kid name is " + ' ' + kids[2])
kids_names("chinna","chinnu","kanna")

"""Arbitrary Arguments are often shortened to *args in Python documentations."""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#4 keyword arguments:You can also send arguments with the key = value syntax.This way the order of the arguments does not matter.

def child_names(child3,child2,child1):
    print("the child once name is" + ' ' + child1)
child_names(child1 = "chinna",child3= "chinnu",child2= "kanna")
#The phrase Keyword Arguments are often shortened to kwargs in Python documentations.


#__________________________________________________________________________________
#Arbitrary Keyword Arguments, **kwargs

"""If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:"""

def myfunction(**colors):
    print("The orange fruit colour is "+ ' ' + colors["colour1"])
myfunction(colour1 = "orange",colour2 =" mango", colour3 = "yellow")
#_ _______________________________ _              _ ____________ _ _______ _ _______ _ ___________
#Default Parameter Value

"""The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:"""

def manoj(colour = "black"):
    print("Manoj skin colour is " + ' ' + colour)
manoj("white")
manoj("brown")
manoj()
#*******************************************************************************
#Passing a List as an Argument
"""You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:"""

def vegitables(food):
    for x in food:
        print(x)
veggies = ["brinzol","potato","brokli","tomato","chilli"]
veggies1 = ("brinzol","potato","brokli","tomato","chilli")
veggies2 = {"brinzol","potato","brokli","tomato","chilli"}
veggies3 = {"name":"pushpa"}
vegitables(veggies)#  here we are passing veggies as an argument to the paramete food(list)
vegitables(veggies1)#tuple
vegitables(veggies2)#set
vegitables(veggies3)#dictionary it will give the  key name

#************_______________________$$$$$$$$$$$$$$$$$$$$$$))))))))))))
# Return value

def value(x):
    return 5 * x
print(value(5))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++

#The pass Statement
"""function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error."""
def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#lambda function : A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a
print(x(5))
