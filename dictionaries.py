"""Dictionaries are used to store data values in key:value pair.
*Dictionaries are ordered ,changeble and do not allow duplicate values
Dictionaries are wriiten with {} curly braces and have keys values

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""
#1  create and print a dictionary

dictionary = {
    'name': 'pushpa',
    'graduation': 'masters',
    'dob': 1996
}
print(dictionary)

#2  dictionary items are in key:value pair and preffered by using key name

print(dictionary['name'])

#3  duplicates are not allowd,Dictionaries cannot have two items with the same key:
thisdictionary = {
    'name': 'pushpa',
    'graduation': 'masters',
    'dob': 1996,
    'dob': 1997
    #Duplicate values will overwrite existing values, the output here will be 1997
}
print(thisdictionary)

#4  Dictionary Length::To determine how many items a dictionary has, use the len() function:
print(len(thisdictionary))#there are four items but the key are duplicated so the output will be 3 only

 #5 Dictionary Items - Data Types: The valuse in dictionaries are any of datatypes

thedict = {
     "name": "pushpa",
     "languages known": ["telugu","hindi","english","marathi"],
     "specification": "Developer",
     "married": False
 }
print(thedict)

#6  type(): From Python's perspective, dictionaries are defined as objects with the data type 'dict':<class 'dict'>
print(type(thedict))

#7 The dict() Constructor: It is also possible to use the dict() constructor to make a dictionary.

dict_constructor = dict(user = "pushpa", dob =1996)#need to use '=' symbol while using a constructor not ':'
print(dict_constructor)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#1   Accessing Items:You can access the items of a dictionary by referring to its key name, inside square brackets:
items = {
"title":"phone",
"model":"samsung",
"price": 15000
}
print(items['price'])
#There is also a method called get() that will give you the same result:
x = items.get('price')
print(x)


#2 Get Keys : The keys() method will return a list of all the keys in the dictionary.
x1 = items.keys()
print(x1)

#3 Get Values : The values() method will return a list of all the values in the dictionary.
x2 = items.values()
print(x2)

#4 Get Items:The items() method will return each item in a dictionary, as tuples in a list.

thedict1 = {

    'name': "manoj",
    'role': "ui developer",
    'age': 24
    }

x33 = thedict1.items()
print(x33)

#5 Check if Key Exists;To determine if a specified key is present in a dictionary use the in keyword:
if 'name' in thedict1:
    print("yes the key is there")
else:
    print("no the key is not there")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#1  Change Items:You can change the value of a specific item by referring to its key name:

fruits = {
    'name': "apple",
    "prize": 800,
    "color": "white",
    "taste": "sweet"
}
fruits['color'] = "red"
print(fruits)

#2 Update Dictionary:The update() method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with key:value pairs.
Thedict = {'name': "apple",
    "prize": 800,
    "color": "white",
    "taste": "sweet"
    }
Thedict.update({'color':'red'})
print(Thedict)


#3 Adding Items:Adding an item to the dictionary is done by using a new index key and assigning a value to it:
additem =  {'name': "apple",
    "prize": 800,
    "color": "white",
    "taste": "sweet"
}
additem['weight'] = "200gm"
print(additem)

#4 Update Dictionary:The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.The argument must be a dictionary, or an iterable object with key:value pairs.
updateitem =  {'name': "apple",
    "prize": 800,
    "color": "white",
    "taste": "sweet"
}
updateitem.update({'weight':'200gm'})
print(updateitem)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#5 Removing Items:
   #pop(): The pop() method removes the item with the specified key name:
popitem = {

     "prize": 800,
    "color": "white",
    "taste": "sweet"
}
popitem.pop('prize')
print(popitem)
   #popitem():The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
popitem.popitem()
print(popitem)
   # The del keyword removes the item with the specified key name:

delitem = {

     "prize": 800,
    "color": "white",
    "taste": "sweet"
}
del delitem['prize']
print(delitem)

    #The del keyword can also delete the dictionary completely:

# delitem1 = {

#      "prize": 800,
#     "color": "white",
#     "taste": "sweet"
# }
# del delitem1
# print(delitem1) #this will cause an error because "thisdict" no longer exists.

   #The clear() method empties the dictionary:

advertiseitem1 = {

     "prize": 800,
    "color": "white",
    "taste": "sweet"
}
advertiseitem1.clear()
print(advertiseitem1)# will return the empty dictionary


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Loop Dictionaries

employee = {

    'name': "manoj",
    "age": 24,
    "gender": "male",

}

for x in employee: 
    #Print all key names in the dictionary, one by one:
    print(x) # for keys to print

    #Print all values in the dictionary, one by one:
    print(employee[x]) # for values to print

#You can also use the values() method to return values of a dictionary:
for x in employee.values():
    print(x)
    #You can use the keys() method to return the keys of a dictionary:
for x in employee.keys():
    print(x)
#Loop through both keys and values, by using the items() method:
for x,y in employee.items():
  print(x,y)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Copy Dictionaries
"""You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy()."""
employee1 = {

    'name': "manoj",
    "age": 24,
    "gender": "male",

}

employee2 = employee1.copy()
print(employee2)

#Another way to make a copy is to use the built-in function dict().
employee3 = dict(employee1)
print(employee3)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Nested Dictionaries: A dictionary can contain dictionaries, this is called nested dictionaries.

myFamily = {

"child1" : {
    "name": "kanna",
    "age": "15"
    },

"child2":{
   "name": "kannaya",
   "age": 10
},

"child3":{
"name":"srusti",
"age":6
    
}

}
print(myFamily)
print(myFamily["child1"])# accesing the child dictionary
print(myFamily["child1"]["name"])# accessing the child dictionay key value



childA = {
    "name": "kanna",
    "age": "15"
    }
childB = {
    "name": "kannaya",
    "age": "15"
    }
childC = {
    "name": "divya",
    "age": "15"
    }

myfamily1 = {
"childA1": childA,
"childA2": childB,
"childA3" : childC

}

print(myfamily1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Dictionary Methods

#clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


#form keys****************
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# dict.fromkeys(keys, value) #syntax


#Same example as above, but without specifying the value:
x1 = ('key1', 'key2', 'key3')

thisdict1 = dict.fromkeys(x1)

print(thisdict1)




#Parameter	Description
# keys	Required. An iterable specifying the keys of the new dictionary
# value	Optional. The value for all keys. Default value is None
