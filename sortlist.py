#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#Sort the list alphabetically:
thelist = ["sanjana","srusti","diva","nandu","kannaya","ganu"]
thelist.sort()
print(thelist)


#Sort the list numerically:
thelist1 = [100,95,86,74,65,51,42,34,29,1]

thelist1.sort()
print(thelist1)
#sort the list in descending order
thelist.sort(reverse = True)
print(thelist)

#reverse()
thelist.reverse()
print(thelist)



#copy() copy of list to newlist1
list = ["hari","manoj","pushpa"]
newlist1 = list.copy()
print(newlist1)


# list() we can use list to get the copy of one variable

#join list(using + , loop ,extend)

list1 = ["hari","manoj","pushpa"]
list2 = [1,2,3,4]
# list3 = list1 + list2
# print(list3)

# for x in list2:
#     list1.append(x)
# print(list1)


list1.extend(list2)
print(list1)

