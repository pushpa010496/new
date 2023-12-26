"""touple are on of inbuilt datatypes of python and other 3 are list,se,dictionary

touples are used to store multiple items in a single variable.these are orderable and unchangebl

these sre written with round brackets

ex: 
tuple = ('latha','pushpa','manoj','hari' )

Tuple items are ordered, unchangeable, and allow duplicate values.
"""
thistuple = ('latha','pushpa','manoj','hari' )
print(thistuple)

#lenth of tuple will be known by len() function

print(len(thistuple))

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple1 = ('latha')
print(type(thistuple1))

thistuple2 = ('latha',)
print(type(thistuple2))

#Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
#A tuple can contain different data types:
tuple13 = ("abc", 34, True, 40, "male")

print(tuple13)

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
thistuple12 = tuple(("apple", "banana", "cherry"))# note the double round-brackets
print(thistuple12)

#Python Collections (Arrays)
"""
List:  Lists are ordered,changeble,allows duplicate values
Dictionaries: Dictionaries are orderd ,changeble, dont allow duplictae values
tuples: these are ordered,unchangeble,allows duplicates
sets: unordered,unchangesble,donr allow duplicates,unindexed
"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Access Tuple Items
#indexing
tuples = ("latha","pushpa",23,True,"manoj","hari")
print(tuples[2])
#negative indexing
print(tuples[-1])
#range of negative indexing
print(tuples[2:5])
print(tuples[-3:-1])#negative indexing may show the last items ,but wen its comes to range i will be in order
print(tuples[:4]) #starts at index 0 and ends at index 3
print(tuples[1:])#strt at index 1 and ends last

#Check if Item Exists
if "pushpa1" in tuples:
    print("yes its there in list")
else:
    print("no its not there in the list")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#update tuples*****
"""Tuples are unchangeable,means onc the tuple is created we cant cremove or add items,tuples are immutable
but there are ways to to it.

Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""

x = ('hari','manoj','pushpa')
y = list(x)
y[1] = 'manoj reddy'
x = tuple(y)
print(x)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Add Items"""""
"""since the tuples rae immutable they are not having inbuilt append() method but there are awys to add items to tuple
1.converts tuple to list and te append a value
2.add tuple to a tuple
"""
#convert into list and append
x1 = ('hari','manoj','pushpa','sridhar')
y1 = list(x1)
y1.append('Akhilesh')
x1 = tuple(y1)
print(x1)


#adding tuple to tuple

x2 = ('hari','manoj','pushpa','sridhar')
y2 = ('Akshay',)
x2 += y2
print(x2)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Remove Items*********
"""tuples are immutable so removing items are not possible ,but there are ways to remove items
1.convert into list and use delete()
2.use del keywor to delete whole tuple
"""
#convert into list and use remove()
x3 = ('hari','manoj''pushpa','sridhar','akhiles')
y3 = list(x3)
y3.remove("akhiles")
x3 = tuple(y3)
print(x3)
#use del keyword

x4=('hari','manoj','pushpa','sridhar','akhiles') 
del x4
#print(x4)#this will raise an error because the tuple no longer exists

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Unpacking a Tuple
"""
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

"""
#unpacking

tuple23 = ('hari','manoj','pushpa','sridhar','akhilesh')

(X,Y,Z,L,M)= tuple23

print(X)
print(Y)
print(Z)
print(L)
print(M)
#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
#USING *Asterisk

tuple231 = ('hari','manoj','pushpa','sridhar','akhilesh')
(a,b,*c) =tuple231
print(a)
print(b)
print(c)

tuple231q = ('hari','manoj','pushpa','sridhar','akhilesh')
(a1,*b1,c1)= tuple231q
print(a1)
print(b1)
print(c1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Loop Through a Tuple
a = ('hari','manoj','pushpa','sridhar','akhilesh')

for x in a:
    print(x)
#loop through indexing
for i in range(len(a)):
    print(a[i])
#using while loop
a1 = (1,2,3,4,5)
i =0
while  i < len(a1):
    print(a1[i])
    i = i+1
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Join Two Tuples********
"""To join two or more tuples you can use the + operator:"""

tupleA = (1,2,3,4,5)
tupleB = ("hari","manoj","pushpa","sridhar")
tupleC = tupleA+tupleB
print(tupleC)

#Multiply Tuples
"""If you want to multiply the content of a tuple a given number of times, you can use the * operator:"""
fruits = ('apple','banana','kiwi','pomogranite')
multiple_tuples = fruits *6
print(multiple_tuples)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#TUPLE METHODS
"""Python has two built-in methods that you can use on tuples.
1.count():Returns the number of times a specified value occurs in a tuple
2.index():Searches the tuple for a specified value and returns the position of where it was found
"""
number = (1,2,3,4,5,6,7,8,9,1,2,3,4,5,6)
new= number.count(2)
print(new)
new1 = number.index(3)
print(new1)