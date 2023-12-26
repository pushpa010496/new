"""pytho has 3 primitive loops
1.while loop: with while loop we can execute the set statements as long as the condition is true.
2.for loop

"""
# i =1 
# while i < 6:
#     print(i)
#     i += 1 # incrementing i is very important if not i will continously execute.
    #Note: remember to increment i, or else the loop will continue forever.


# break statement:With the break statement we can stop the loop even if the while condition is true:


# i = 1
# while i <6 :
#     print(i)
#     if i == 3: 
#      break #Exit the loop when i is 3:
#     i = i+1 
    


#The continue Statement: With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i <6:
    i +=1
    if i == 3:
        continue
    print(i)


#The else Statement:With the else statement we can run a block of code once when the condition no longer is true:
i = 1 
while i <6:
    print(i)
    i+= 1
else:
    print("i is less than 6 ")



