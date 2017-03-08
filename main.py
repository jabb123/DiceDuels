print("Welcome to dice duels")
from random import randrange

player1w =0 
player2w =0 
player1w!=0 and player2w!=0 
while(player1w!=2 and player2w!=2):
	raw_input("press enter to roll dice")
	roll1= randrange(0,6)
	print(roll1)
	roll2= randrange(0,6)
	if (player1w>player2w):
		player1w +=1
		print("Player one wins the round!")
	else (player2w>player1w):
		player2w +=1
		print("Player two wins the round!")
	if player1w ==2:
		print("Player one wins the game!")
	else player2w ==2:
		print("Player two wins the game!")


