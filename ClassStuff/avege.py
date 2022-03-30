import os
#Maria I Suarez
# Jan 14, 2022
# Declare variables, print variables, print type of data,  
# learn some operators

# this symbol is fo comments, means the computer will ignore
# I want clear my terminal
os.system('cls')
#Program is Average of 3 tests

#
#Declare and Assign values
test1=89
test2=78.5
test3=86
Flag=False

#to diplay things on the screen we use the function print()
# print(type(test1), type(test2), type(Flag))

#declare Sum to add tests symbol for addition is  +
Sum = test1 + test2 + test3
#Average we will division ....     /
Average= Sum/3
print(Average)

#I want to print    The average of 3 tests is " number here"

print("Test1 =", test1, end=" ")
print("Test2", test2)
print("The average of 3 tests is", Average)