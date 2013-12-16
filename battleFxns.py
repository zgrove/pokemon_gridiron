#!/usr/bin/env python3

from math import floor
from random import randint
import classes

#print randint(217, 255)

def dealDamage(level, attackStat, attackPower, defPokeDefense, stab, effectiveness):
	"""This fxn calculates & returns how much damage the attacking Pokemon deals the defending Pokemon"""
	r = random.randint(217, 255)
	damage = math.floor(((((2*level/5+2)*attackStat*attackPower/defPokeDefense)/50)+2)*stab*effectiveness*r/255)
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
	# Fire Move
	if moveType == classes.Types[0]:
		if defPoketype1 == classes.Types[0] or defPoketype2 == classes.Types[0]:
			effectiveness = 0.5
		elif defPoketype1 == classes.Types[1] or defPoketype2 == classes.Types[1]:
			effectiveness = 0.5
		elif defPoketype1 == classes.Types[2] or defPoketype2 == classes.Types[2]:
                        effectiveness = 2
		else:
			effectiveness = 1
	# Water Move
	if moveType == classes.Types[1]: 
                if defPoketype1 == classes.Types[0] or defPoketype2 == classes.Types[0]:
                        effectiveness = 2
                elif defPoketype1 == classes.Types[1] or defPoketype2 == classes.Types[1]:
                        effectiveness = 0.5
                elif defPoketype1 == classes.Types[2] or defPoketype2 == classes.Types[2]:
                        effectiveness = 0.5  
                else:   
                        effectiveness = 1
	# Grass Move
	if moveType == classes.Types[2]: 
                if defPoketype1 == classes.Types[0] or defPoketype2 == classes.Types[0]:
                        effectiveness = 0.5
                elif defPoketype1 == classes.Types[1] or defPoketype2 == classes.Types[1]:
                        effectiveness = 2
                elif defPoketype1 == classes.Types[2] or defPoketype2 == classes.Types[2]:
                        effectiveness = 0.5  
                else:   
                        effectiveness = 1
	return effectiveness
