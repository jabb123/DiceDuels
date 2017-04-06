print("Welcome to dice duels")
from random import randrange
ctr=0
player1=str(raw_input("player 1 enter name-\n"))
player2=str(raw_input("player 2 enter name-\n"))

player1w =0 
player2w =0 
while(ctr!=10):
	while(player1w!=3 and player2w!=3):
		raw_input("press enter to roll dice-\n")
		roll1= randrange(1,11)
		print(player1 + " rolled a " + str(roll1))
		print("")
		roll2= randrange(1,11)
		print(player2 + " rolled a " + str(roll2))
		print("")
		if (roll1>roll2):
			player1w +=1
			print(player1 + " wins the round!\n")
		elif(roll1<roll2):
			player2w +=1
			print(player2 + " wins the round!\n")
	if player1w ==3:
		print(player1 + " wins the game!\n")
		playagain=raw_input("If you want to play again type yes, if not type no.\n")
		if(playagain=="yes"):
			ctr=1
			player1w=0
			player2w=0
		if(playagain=="no"):
			ctr=10
	if player2w ==3:
		print(player2 + " wins the game!\n")
		playagain=raw_input("If you want to play again type yes, if not type no.\n")
		if(playagain=="yes"):
			ctr=1
			player1w=0
			player2w=0
		if(playagain=="no"):
			ctr=10

