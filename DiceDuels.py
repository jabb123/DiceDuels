print("Dice Roller Game")
print("two players roll the dice and see who can get higher number, best of three wins")
from random import randrange 

print("Player1 first dice roll")
Roll1= randrange(1,6)
print(Roll1)

print("Player2 first dice roll")
Roll2= randrange(1,6)
print(Roll2)

print("Player1 second dice roll")
Roll3= randrange(1,6)
print(Roll3)

print("Player2 second dice roll")
Roll4= randrange(1,6)
print(Roll4)

if(Roll1 > Roll2 and Roll3 > Roll4):
	print("Player1 wins!")