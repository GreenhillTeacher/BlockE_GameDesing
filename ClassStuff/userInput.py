#MAria Suarez
#01/21/22

#We are going to learm the input() function, random numbers
# type casting, branching. looping
import os, random
os.system('cls')
#declare variable for user input
# print("enter a number from 1-10: ", end="")
# useless=int(input())  #input returns a string we must type cast if we need a number
# print("The number is %.2f " %(useless/3))
# guess=int(input("PLease give a number "))

#guess a number
#myNumber = 9 instead of using a fix number we will use random
myNumber=random.randint(1,10)
print("#################################################")
print("#                                               #")
print("#            guess a number                      #")
GameOn=True
while(GameOn):
    userGuess=int(input("Guess anumber from 1-10 "))
    if myNumber ==userGuess:
        print("You guessed it!")
        GameOn=False
    else:
        print("good luck next time")
print("The number to guess was "+ str(myNumber))
