#!/usr/bin/env python

'''
Game of Sticks:
Human v. AI Sticks
Hat Tip: http://nifty.stanford.edu/2014/laaksonen-vihavainen-game-of-sticks/handout.html

Table of contents:
1.   Import modules.
2.   Initialize global Variables.
3.   Introduction to the game.
4.   Instructions to the game.

'''

import random
import sys

#Global Variables used throughout
prompt = '>>> ' 
btw_10_100 = 'Please pick a number between 10 and 100'
btw_1_3 = 'Please pick a number beteween 1 and 3.'
play_again_msg = 'Play again (1 = yes, 0 = no)?'
value_error_msg = 'Oops! Something went wrong. Please pick a NUMBER.'


#Introduction to the game
raw_input("Welcome to the game of sticks! Press <Enter> to continue...")

#Add instructions
while True:
	print("Do you want the instructions for how to play sticks? Y/N")
	instructions_ans = raw_input(prompt)

	if instructions_ans.upper() == 'Y':
		print '''
		In the game of sticks you have two players and X sticks. Each player
		takes turns and picks up between 1 to 3 sticks on their turn. The 
		game continues until there is one stick left and the player who picks
		up that stick loses.
		'''
		break

	elif instructions_ans.upper() == 'N':
		break

	else:
		print "Please answer with a Y or N."

while True:
	try:
		print("How many sticks are there on the table initially (10-100)?")
		num_sticks = int(raw_input(prompt))
		reset = num_sticks

		if 10<=num_sticks<=100:
			print("Ok, there are %s sticks on the board.") % (num_sticks)
			print("|")*num_sticks
			break
		else:
			print (btw_10_100)
	except ValueError:
		print value_error_msg		

#Initialize a dictionary that we will add to in the loop
stick_dict={}
for number in range(1,num_sticks+1):
	stick_dict["hat{0}".format(number)]=[[1,2,3]]


#Create an "infinite loop" so the program will continue to iterate
while True:
	while num_sticks!=0:
        
        #####################
		###### PLAYER 1 #####
		#####################

		#Continues to iterate until you give a number between 1 and 3
		while True:
			try:
				print "Player 1: How many sticks do you take (1-3)?"
				player_1 =  int(raw_input(prompt))
				
				if 1 <= player_1 <= 3:
					break
				else:
					print (btw_1_3)
			except ValueError:
				print value_error_msg	

		#Takes the user input and calculates the new number of sticks
		num_sticks = num_sticks - player_1

		#Different messages for different conditions
		if num_sticks == 1:
			print("Ok, there is %s stick on the board.") % (num_sticks)
			print("|")*num_sticks

		##### Important ##### 
		#If Player 1 loses, then we keep the proper values
		elif num_sticks < 1:
			print("Player 1, you lose.")

			#If Player 1 loses, then the AI wins and we want to execute this 
			for key in stick_dict:
				if len(stick_dict[key]) == 2:
					stick_dict[key][0].append(stick_dict[key][1])
					del stick_dict[key][1]
					num_sticks = reset
					print stick_dict

		#Keep playing
		else:
			print("Ok, there are %s sticks on the board.") % (num_sticks)
			print("|")*num_sticks


        ######################
		###### AI Player #####
		######################

		#Random guess generator
		guess = random.choice(stick_dict["hat{0}".format(num_sticks)][0])
		if guess > 1:
			print "The computer chose %s sticks" % (guess)
		elif guess == 1:
			print "The computer chose %s stick" % (guess)

		#Append that guess to a list that corresponds with the proper "hat"
		stick_dict["hat{0}".format(num_sticks)].append(guess)
		#print stick_dict

		#Calculates the number of sticks after the computer's guess
		num_sticks = num_sticks - guess


		if num_sticks == 1:
			print("Ok, there is %s stick on the board.") % (num_sticks)
			print("|")*num_sticks

		##### Important #####
		#Here the AI loses, we delete its guesses, and reset num_sticks
		elif num_sticks < 1:
			print("Player 2 (AI BOT), you lose.")
			#If the AI loses
			for key in stick_dict:
				if len(stick_dict[key]) == 2:
					del stick_dict[key][1]
					num_sticks = reset
					print stick_dict
			#print(play_again_msg)
			#play_again_binary = int(raw_input(prompt))

		else:
			print("Ok, there are %s sticks on the board.") % (num_sticks)
			print("|")*num_sticks


	










