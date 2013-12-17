#!/usr/bin/env python3

from classes import *
import time
from random import randint
from battleFxns import *

def battle(player_Pokemon, rival_name, opponent_Pokemon):

	player_current_Pokemon = player_Pokemon[0]
	opponent_current_Pokemon = opponent_Pokemon[0]

	print("You sent out " + player_current_Pokemon.getName() + "!")
	time.sleep(2)
	print()
	print("Your rival " + rival_name + " sent out " + opponent_current_Pokemon.getName() + "!")
	time.sleep(2)
	print()
	printHp(player_current_Pokemon, opponent_current_Pokemon)

	while not allFainted(player_Pokemon) and not allFainted(opponent_Pokemon):
		player_move = getMove()
		opponent_move = randint(1, 4)
			
		if (player_move > -1):
			if (player_current_Pokemon.getStats().getSpeed() >= opponent_current_Pokemon.getStats().getSpeed()):
				print(player_current_Pokemon.getName() + " used " + player_current_Pokemon.getMove(player_move).getName() + "!\n")
				time.sleep(2)
				damage = doDamage(player_current_Pokemon, opponent_current_Pokemon, player_move)
				opponent_current_Pokemon.takeDamage(damage)
				printHp(player_current_Pokemon, opponent_current_Pokemon)
				print()
				if (not opponent_current_Pokemon.isFainted()):
					print("Rival " + rival_name + "'s " + opponent_current_Pokemon.getName() + " used " +
						opponent_current_Pokemon.getMove(opponent_move).getName() + "!\n")
					time.sleep(2)
					damage = doDamage(opponent_current_Pokemon, player_current_Pokemon, opponent_move)
					player_current_Pokemon.takeDamage(damage)
					printHp(player_current_Pokemon, opponent_current_Pokemon)
					if (player_current_Pokemon.isFainted()):
						print("Your " + player_current_Pokemon.getName() + " fainted!")
						time.sleep(2)
						print()
				else:
					print("Rival " + rival_name + "'s " + opponent_current_Pokemon.getName() + " fainted!")
					time.sleep(2)
					print()
				
			else:
				print("Rival " + rival_name + "'s " + opponent_current_Pokemon.getName() + " used " +
                                        opponent_current_Pokemon.getMove(opponent_move).getName() + "!\n")
				time.sleep(2)
				damage = doDamage(opponent_current_Pokemon, player_current_Pokemon, opponent_move)
				player_current_Pokemon.takeDamage(damage)
				printHp(player_current_Pokemon, opponent_current_Pokemon)
				print()
				if (not player_current_Pokemon.isFainted()):
					print(player_current_Pokemon.getName() + " used " + player_current_Pokemon.getMove(player_move).getName() + "!\n")
					time.sleep(2)
					damage = doDamage(player_current_Pokemon, opponent_current_Pokemon, player_move)
					opponent_current_Pokemon.takeDamage(damage)
					printHp(player_current_Pokemon, opponent_current_Pokemon)
					print()
					if (opponent_current_Pokemon.isFainted()):
						print("Rival " + rival_name + "'s " + opponent_current_Pokemon.getName() + " fainted!")
						time.sleep(2)
						print()
				else:
					print("Your " + player_current_Pokemon.getName() + " fainted!")
					time.sleep(2)
					print()
		else:
			for i in range(1, 5):
				print(str(i) + ". " + player_current_Pokemon.getMove(i).getName() + ":     \tPow: " + str(player_current_Pokemon.getMove(i).getPower()) +
					"  \tAcc: " + str(player_current_Pokemon.getMove(i).getAccuracy()))
			print()

	if (allFainted(player_Pokemon)):
		print("Rival " + rival_name + ": Ha! That was too easy! I'll smell you later!")
	elif (allFainted(opponent_Pokemon)):
		print("Rival " + rival_name + ": What?! That's impossible! How could I lose to you?")

def doDamage(pokemon1, pokemon2, move):
	stab = calcSTAB(pokemon1.getType1(), pokemon1.getMove(move).getType()) * calcSTAB(pokemon1.getType2(), pokemon1.getMove(move).getType())
	eff = calcEffectiveness(pokemon1.getMove(move).getType(), pokemon2.getType1(),
		pokemon2.getType2())
	if (pokemon1.getMove(move).getCategory() == "Physical"):
		attack = pokemon1.getStats().getAttack()
		defense = pokemon2.getStats().getDefense()
	else:
		attack = pokemon1.getStats().getSpAttack()
		defense = pokemon2.getStats().getSpDefense()
	damage = dealDamage(pokemon1.getLevel(), attack, pokemon1.getMove(move).getPower(),
		defense, stab, eff)
	return damage

def allFainted(pokemon_party):

	for pokemon in pokemon_party:
		if not pokemon.isFainted():
			return False

	return True

def printHp(player_current_Pokemon, opponent_current_Pokemon):
	print(player_current_Pokemon.getName() + "     [" + str(player_current_Pokemon.getCurrentHp()) + " / " +
                str(player_current_Pokemon.getStats().getHp()) + "]\t\t" + opponent_current_Pokemon.getName() + "     [" +
                str(opponent_current_Pokemon.getCurrentHp()) + " / " + str(opponent_current_Pokemon.getStats().getHp()) + "]")

def getMove():

	while True:
		command = input("\nCommands:\n\tbattle\n\tbag\n\tparty\n\trun\n\nWhat will you do? ").split(" ")
		print()
		if command[0] == "battle":
			if len(command) <= 1:
				print("battle [options] [input] \n\nOptions:\n\t-s\tShow the moves of your POKEMON " +
                                        "(takes no input)\n\t-u\tUse the move (1-4) given in the input\nExample:\tbattle -u 3 (Uses move 3)")
			elif command[1] == "-s":
				return -1
			elif command[1] == "-u":
				try:
					if int(command[2]) < 1 or int(command[2]) > 4:
						print("Please enter a move between 1-4")
					else:
						return int(command[2])
				except ValueError:
					print("Please enter a move between 1-4")
			else:
				print("battle [options] [input] \n\nOptions:\n\t-s\tShow the moves of your POKEMON " +
					"(takes no input)\n\t-u\tUse the move (1-4) given in the input\n\nExample:\tbattle -u 3 (Uses move 3)")
		elif command[0] == "bag":
			print("You don't have anything in your bag!")
		elif command[0] == "party":
			print("You don't have any other POKEMON in your party!")
		elif command[0] == "run":
			print("There's no running from a POKEMON battle!")
		else:
			print("The command you entered is not valid.")
