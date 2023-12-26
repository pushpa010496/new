thelist = ["hari","manoj","sai","shiv"]
newlist = []
for x in thelist:
    if "i" in x:
        newlist.append(x)
print(newlist)

#list comprehension

thelist1 = ["hari","manoj","sai","shiv"]
newlist1 = [x for x in thelist1 if "a" in x]
print(newlist1)

newlist2 = [x for x in range(10)]
print(newlist2)
newlist4 = [x for x in range(10) if x<5]
print(newlist4)

newlist3 = [x for x in thelist1 if x!="manoj"]
print(newlist3)

newlist4 = [x.upper() for x in thelist1]
print(newlist4)

newlist5 = ["hello" for x in thelist1 ]
print(newlist5)

newlist6 = [x if x!="hari" else "harinath" for x in thelist1]
print(newlist6)

