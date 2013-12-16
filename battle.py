
def battle(player_Pokemon, rival_name, opponent_Pokemon):

	player_current_Pokemon = player_Pokemon[0]
	opponent_current_Pokemon = opponent_Pokemon[0]

	print("You sent out " + player_current_Pokemon.getName() + "!")
	print("Your rival " + rival_name + " sent out " + opponent_current_Pokemon.getName() + "!")
	print()
	print(player_current_Pokemon.getName() + "     " + player_current_Pokemon.getCurrentHp() + " / " + player_current_Pokemon.getHp())

	while not allFainted(player_Pokemon) and not allFainted(opponent_Pokemon):
		player_move = getMove()
		if player_move == 1:
			print("Charizard used Flamethrower!")
		elif player_move == 2:
			print("Charizard used Air Slash!")
		elif player_move == 3:
			print("Charizard used Dragon Pulse!")
		elif player_move == 4:
			print("Charizard used Earthquake!")
		else:
			print("Something went wrong...")

def allFainted(pokemon_party):

	for pokemon in pokemon_party:
		if not pokemon.fainted():
			return False

	return True

def getMove():

	while True:
		command = input("What will you do? ").split(" ")
		if command[0] == "battle":
			if command[1] == "-s":
				print("Print the moves.")
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
					"(takes no input)\n\t-u\tUse the move (1-4) given in the input\nExample:\tbattle -u 3 (Uses move 3)")
		elif command[0] == "bag":
			print("You don't have anything in your bag!")
		elif command[0] == "party":
			print("You don't have any other POKEMON in your party!")
		elif command[0] == "run":
			print("There's no running from a POKEMON battle!")
		else:
			print("The command you entered is not valid.")
