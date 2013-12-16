#!/usr/bin/env python3

import pokemon_choose

def prebattle(rival_name):
	"""This fxn allows the user and rival to choose a Pokemon"""
	decision = 'n'
	while decision != 'y':
		print ("Please choose a Pokemon to be your partner:")
		print()
		for items in pokeList:
			print (items)
		print ()
		validChoice = False
	
		userPoke = input()

		while validChoice == False:
			for items in pokeList:
				temp = items
				if temp == userPoke:
					validChoice = True
			if validChoice == False:
				print ()
				print ("That Pokemon is not discovered yet. Please choose one of the following:")
				print ()
				for items in pokeList:
					print (items)
				print ()
				userPoke = input()
		decision = input ("So you choose " + userPoke + "? ('y' or 'n') ")

pokeList = ["Venusaur", "Charizard", "Blastoise", "Pikachu", "Machamp", "Dragonite"]
