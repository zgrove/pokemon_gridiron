#!/usr/bin/env python3

from pokemon_choose import *
from random import randint
import time

nameList = ["Venusaur", "Charizard", "Blastoise", "Pikachu", "Dragonite", "Machamp"]

def prebattle(rival_name):
	"""This fxn allows the user and rival to choose a Pokemon"""
	decision = 'n'
	while decision != 'y':
		print ("Please choose a POKEMON to be your partner:")
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
				print ("That POKEMON is not discovered yet. Please choose one of the following:")
				print ()
				for items in pokeList:
					print (items)
				print ()
				userPoke = input()
		decision = input ("So you choose " + userPoke + "? ('y' or 'n') ")
	
	randomName = userPoke
	while randomName == userPoke:
		randomName = nameList[randint(0, 5)]

	print()
	A_button = input("Rival " + rival_name + ": OK! Well, I chose " + pokeList[randomName].getName() + "!")
	A_button = input("Rival " + rival_name + ": He's obviously gonna trump your weak little " + pokeList[userPoke].getName() + "!")
	A_button = input("Rival " + rival_name + ": Let's battle!")
	time.sleep(0.5)
	print(".")
	time.sleep(0.5)
	print(".")
	time.sleep(0.5)
	print(".")
	print()

	return [pokeList[userPoke], pokeList[randomName]]
