"""variable name can start with letter or character
variable name shoud only have _,leters,number 

variable names are case sensitive
 """

x,y,z = "pushpa",5,20.2 #multiple valuse to multiple variables
print(x,y,z)
print(y)
print(z)


x=y=z=5 #assigning one values to multiple variables
print(x,y,z)
print(x)

fruits = ["apple","banana","orange"] # unpacking a collection
x,y,z= fruits
print(x,y,z)
print(y)

#output variable is print()

x= 5
y= 9
print(x+y) #give the rsult as addiation of x and y

x="chinna "
y="chinnu"
print(x+y)#add the string

# x=6
# y="chinna"
# print(x+y)#give the error,cant add the strimg and int value

"""global variables"""
"""global variables are variables which created outside of the funtion.Global variables can be used by everyone, both inside of functions and outside."""

x= "awsome"

def myfunction():
    x="fantastic"
    print("python is " + x)
myfunction()
print("python is "+ x)
"""If you use the global keyword, the variable belongs to the global scope:"""

x="123"
def myfunction1():
    global x
    x="fantastic"
myfunction1()

print(x)