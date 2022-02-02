#MariaSuarez 
# 01/31/2022
# Strings array of characters
#Has many functions

import os, random
os.system('cls')
myName= "Maria Suarez"
myStatement=""" My name is  
so nice because
b;ah blah blagggg 
 
what vever 
ever""" 
for elem in myName:
    print(elem, end=" ")
guess=random.choice(myName)
print(guess)
words=["Radio", "Clues", "suite", "peter", "robot"]
word=random.choice(words)
print(word)
check=True
while check:
    letter=input("Dear user, please give us a nice letter ")
    if len(letter)>1 or not letter.isalpha():
        print("BAd")
    else:
        check=False
print("ready to play te game")
for i in range(len(word)):
    if letter == word[i]:
        print(letter, end= " ")
    else:
        print("_", end=" ")

# print ("My last name begins with " +myName[6 ])
# print(myStatement) 
# if 'blah' in myStatement: 
#     print('true') 
# print('expert' not in myStatement) 
# # find() will return the index of the chraracter you are looking for(first instance) 
# INDEX= myName.find("a")
# print(INDEX)
# #finding the lenght of your word
# wordLen=len(myName)
# print(wordLen) #your last index is len-1
# #For loop in range 0 to limit
# for i in range(wordLen-1):
#     if "a" in myName[i]:
#         print(i, end=", ")
# print("")
# print("done")
# myStatement=myStatement.upper() #make all letter upper case
# print(myStatement)


