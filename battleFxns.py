#!/usr/bin/env python3

from math import floor
from random import randint
import classes

types = {'Fire': [['Grass', 'Bug', 'Ice', 'Steel'], ['Fire', 'Water', 'Rock', 'Dragon'], []],
         'Water': [['Fire', 'Ground', 'Rock'], ['Water', 'Grass', 'Dragon'], []],
         'Grass': [['Water', 'Ground', 'Rock'], ['Fire', 'Grass', 'Flying', 'Poison', 'Bug', 'Dragon', 'Steel'], []],
         'Electric': [['Water', 'Flying'], ['Grass', 'Electric', 'Dragon'], ['Ground']],
         'Normal': [[], ['Rock', 'Steel'], ['Ghost']],
         'Fighting': [['Normal', 'Rock', 'Ice', 'Steel', 'Dark'], ['Flying', 'Poison', 'Bug', 'Psychic'], ['Ghost']],
         'Flying': [['Grass', 'Fighting', 'Bug'], ['Electric', 'Rock', 'Steel'], []],
         'Poison': [['Grass'], ['Poison', 'Ground', 'Rock', 'Ghost'], ['Steel']],
         'Ground': [['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], ['Grass', 'Bug'], ['Flying']],
         'Rock': [['Fire', 'Flying', 'Bug', 'Ice'], ['Fighting', 'Ground', 'Steel'], []],
         'Bug': [['Grass', 'Psychic', 'Dark'], ['Fire', 'Fighting', 'Flying', 'Poison', 'Ghost', 'Steel'], []],
         'Ghost': [['Ghost', 'Psychic'], ['Steel', 'Dark'], ['Normal']],
         'Psychic': [['Fighting', 'Poison'], ['Psychic', 'Steel'], ['Dark']],
         'Ice': [['Grass', 'Flying', 'Ground', 'Dragon'], ['Fire', 'Water', 'Ice', 'Steel'], []],
         'Dragon': [['Dragon'], ['Steel'], []],
         'Steel': [['Rock', 'Ice'], ['Fire', 'Water', 'Electric', 'Steel'], []],
         'Dark': [['Ghost', 'Psychic'], ['Fighting', 'Steel', 'Dark'], []]}

def dealDamage(level, attackStat, attackPower, defPokeDefense, stab, effectiveness):
	"""This fxn calculates & returns how much damage the attacking Pokemon deals the defending Pokemon"""
	r = randint(217, 255)
	damage = floor(((((2*level/5+2)*attackStat*attackPower/defPokeDefense)/50)+2)*stab*effectiveness*r/255)
	return damage

def calcSTAB(pokeType, moveType):
	"""This fxn calculates Same Type Attack Bonus
	STAB = 1.5 if the Pokemon's type is the same as the intended move's type"""
	if pokeType == moveType:
		stab = 1.5
	else:
		stab = 1
	return stab

def calcEffectiveness(moveType, defPokeType1, defPokeType2):
	"""This fxn determines if the attack is 'not very effective', 'super effective', etc."""

	move_effect = types[moveType]
	effectiveness = 1

	if defPokeType1 in move_effect[0]:
		effectiveness = effectiveness * 2
	elif defPokeType1 in move_effect[1]:
		effectiveness = effectiveness * 0.5
	elif defPokeType1 in move_effect[2]:
		effectiveness = effectiveness * 0

	if defPokeType2 in move_effect[0]:
		effectiveness = effectiveness * 2
	elif defPokeType2 in move_effect[1]:
		effectiveness = effectiveness * 0.5
	elif defPokeType2 in move_effect[2]:
		effectiveness = effectiveness * 0

	if effectiveness > 1:
		print ("It's super effective!")
	elif effectiveness == 0.5:
		print ("It's not very effective...")
	elif effectiveness == 0:
		print ("It has no effect...")

	print()

	return effectiveness
