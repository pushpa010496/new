
"""Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application."""




# import modules


# modules.mymodule('chinna') #Note: When using a function from a module, use the syntax: module_name.function_name.
# a = modules.person1["age"]
# print(a)

#Re-naming a Module:import mymodule as mx

import modules as mx
mx.mymodule('chinna')
a= mx.person1['age']
print(a)

#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Built-in Modules:There are several built-in modules in Python, which you can import whenever you like.
#Import and use the platform module:

import platform

x = platform.system()
print(x)
#   *******************************************************************

#Using the dir() Function:There is a built-in function to list all the function names (or variable names) in a module. The dir() function:


x1 = dir(platform)
print(x1)