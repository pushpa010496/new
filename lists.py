listexample = ['hari','akhil','manoj','pushpa','hari1','akhil2','manoj3','pushpa4']
print(len(listexample))
print(type(listexample))
print(listexample[-5:-2])
print(listexample[2:])
print(listexample[:-2])
# print(listexample[5:2])
if "hari" in listexample:
    print("yes hari is in the list") 

listexample[1]= "akhilesh"
print(listexample)
print(listexample[1])
listexample[1:3] =["chinna","chinnu","nani"]
print(listexample)

#insert() #can only add for specific index
listexample.insert(2,"shiv")
print(listexample)

#append() it will add exactly one element at te end of the list
listexample.append('sai')
print(listexample)

#extend()

newlist=[1,3,4]
listexample.extend(newlist)
print(listexample)

#remove()
listexample.remove('shiv')#if we give more than 1 value it will through error
print(listexample)

#pop()
listexample.pop() #if you dont specify the index it will remove the last item
print(listexample)

listexample.pop(1)
print(listexample)

#del() will delete the list completely if you dont specify the index

# del listexample[3]
# print(listexample)

# del listexample
# print(listexample)

#clear() The clear() method empties the list.The list still remains, but it has no content.

newlist1 = ['manoj','hari']
newlist1.clear()
print(newlist1)
newlist1.append('hari')
print(newlist1)
newlist1.insert(1,2)
print(newlist1)


#looplist

thislist = ["hari","manoj","harinath","manojreddy"]
for i in thislist:
 print(i)

#using while loop
thislist1 = ["hari","manoj","harinath","manojreddy"]
i=0
while i<len(thislist1):
    print(thislist1[i])
    i= i+1

#short hand for loop

thislist2 = ["hari","manoj","harinath","manojreddy"]
[print(x) for x in thislist2]

thislist3 = [1,2,3,4,5,6]
[print(x) for x in thislist3]