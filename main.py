print("Welcome to dice duels")
from random import randrange

player1=str(raw_input("player 1 enter name-"))
player2=str(raw_input("player 2 enter name-"))

player1w =0 
player2w =0 
while(player1w!=3 and player2w!=3):
	raw_input("press enter to roll dice-")
	roll1= randrange(1,7)
	print(roll1)
	roll2= randrange(1,7)
	print(roll2)
	if (roll1>roll2):
		player1w +=1
		print(player1 + " wins the round!")
	elif(roll1<roll2):
		player2w +=1
		print(player2 + " wins the round!")
if player1w ==3:
	print(player1 + " wins the game!")
if player2w ==3:
	print(player2 + " wins the game!")