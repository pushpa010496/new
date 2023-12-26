"""Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.


* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.{}

"""
sets = {"apple","banana","kiwi",1,2, True}# Set items can be of any data type:
print(sets)

# Duplicates are not allowed
set1 =  {"apple","banana","kiwi",1,2, True,1,2,"apple"} # sets are consider True and 1 are same so it will cosider duplicate if both are present in the set and give only one value in the output
print(set1)
print(type(set1))#From Python's perspective, sets are defined as objects with the data type 'set':

#set CONSTRUCTOR

seta = set((2,3,4,5,6,1,2,3))#output will be set
print(seta)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Access Items
"""You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword."""

fruits = {"apple","banana","kiwi","orange","apple"}
for x in fruits:
    print(x)

print("banana" in fruits)  #out put will be True  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Add Items
"""Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method.
"""

fruit = {"banana","apple","apple"}
fruit.add("orange")
print(fruit)

#Add Sets
"""To add items from another set into the current set, use the update() method."""
fruit1 = {"apple","banana"}
fruit2 = {"orange","kiwi"}
fruit1.update(fruit2)
print(fruit1)

#Add Any Iterable
"""the object in the update() method does not hav eto be a set it can be any iterbale(list,tuple,dictionary) """

setA = {"APPLE",1,True,False,"west","apple"}#case sensitive
list = [1,2,"orange","banana",True,False]
setA.update(list)
print(setA)

#Remove Item
"""To remove an item in a set, use the remove(), or the discard() method."""
setA1 = {"APPLE",1,True,False,"west","apple"}
setA1.remove("apple")
print(setA1)
# setA1.remove(2)#Note: If the item to remove does not exist, remove() will raise an error.
# print(setA1)

#Remove "banana" by using the discard() method:
setA2 = {"APPLE",1,True,False,"west","apple"}
setA2.discard("apple")
print(setA2)
setA2.discard(1)
print(setA2)
setA2.discard(2)#Note: If the item to remove does not exist, discard() will NOT raise an error.
print(setA2)

"""You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item."""

#Remove a random item by using the pop() method:
setA3 = {1,2,3,4,"true",True}
setA3.pop()
print(setA3)

#The clear() method empties the set:
setA4 = {1,2,3,4,"true",True}
setA4.clear()
print(setA4)

#The del keyword will delete the set completely:
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)#this will raise an error because the set no longer exists

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Loop Items
"""You can loop through the set items by using a for loop:"""
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Join Two Sets
#******************
"""There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:"""

#The union() method returns a new set with all items from both sets:

set_a = {"hari","manoj","pushpa"}
set_b = {1,2,3,4,5}
set_c = set_a.union(set_b)
print(set_c)

#The update() method inserts the items in set2 into set1:
set_d = {"hari","manoj","pushpa"}
set_e = {1,2,3,6,4,5,8}
set_d.update(set_e)
print(set_d)

#Keep ONLY the Duplicates
"""The intersection_update() method will keep only the items that are present in both sets."""
#Keep the items that exist in both set x, and set y:
x = {"apple","banana","orange"}
y = {"kiwi","grapes","banana"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
x1 = {"apple","banana","orange"}
y1 = {"kiwi","grapes","banana"}
z = x1.intersection(y1)
print(z)


#Keep All, But NOT the Duplicates
"""The symmetric_difference_update() method will keep only the elements that are NOT present in both sets."""
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
x2.symmetric_difference_update(y2)
print(x2)

"""The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets."""
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
z2 = x2.symmetric_difference(y2)
print(z2)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#set methods
#method    Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others