#!/usr/bin/env python3

Types = ['Fire', 'Water', 'Grass', 'Electric', 'Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Psychic', 'Ice', 'Dragon', 'Steel', 'Dark', 'None']

class Stats(object):
	"""Constructs a class for the Pokemon's stats"""

	def __init__(self, hp, attack, defense, spAttack, spDefense, speed):
		"""Init method for initializing Stats Class"""
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.spAttack = spAttack
		self.spDefense = spDefense
		seld.speed = speed

	def getHp(self):
		"""Returns HP"""
		return self.hp

	def getAttack(self):
		"""Returns Attack"""
		return self.attack

	def getDefense(self):
		"""Returns Defense"""
		return self.defense

	def getSpAttack(self):
		"""Returns Special Attack"""
		return self.spAttack

	def getSpDefense(self):
		"""Returns Special Defense"""
		return self.spDefense

	def getSpeed(self):
		"""Returns Speed"""
		return self.speed

	def __str__(self):
		"""Prints out all stats in organized manner"""
		print ("HP: " + self.hp)
		print ("Attack: " + self.attack)
		print ("Defense: " + self.defense)
		print ("Special Attack: " + self.spAttack)
		print ("Special Defense: " + self.spDefense)
		print ("Speed: " + self.speed)

class Pokemon(object):
	"""Describes a Pokemon"""
	
	def __init__(self, name, type1, type2, moves, stats):
		"""Init method for initializing Pokemon Class"""
		self.name = name
		self.level = 50
		self.type1 = type1
		self.type2 = type2
		self.moves = moves
		self.currentHp = stats.getHp()
		self.faint = False

	def getName(self):
		"""Returns Pokemon's name"""
		return self.name

	def getLevel(self):
		"""Returns a Pokemon's level"""
		return self.level

	def getType1(self):
		"""Returns a Pokemon's 1st type"""
		return self.type1

	def getType2(self):
		"""Returns a Pokemon's 2nd type"""
		return self.type2

	def getMove(self, index):
		"""Returns a Pokemon's move (1-4 depending on index value)"""
		return moves.get(index)

	def getStats(self):
		"""Returns a Pokemon's stats"""
		return stats

	def getCurrentHp(self):
		"""Returns Pokemon's current HP"""
		return self.currentHp

	def getFaint(self):
		"""Returns Pokemon's Faint status"""
		return self.faint
	
	def fainted(self):
		"""Sets Pokemon's Faint status to True"""
		self.faint = True

class Move(object):
	"""Describes a move a Pokemon can use"""

	def __init__(self, name, type, power, accuracy, description, category):
		"""Initializes Pokemon move"""
		self.name = name
		self.type = type
		if power < 0:
			self.power = 0
		elif power > 250:
			self.power = 250
		else:
			self.power = power
		if accuracy < 50:
			self.accuracy = 50
		elif accuracy > 100:
			self.accuracy = 100
		else:
			self.accuracy = accuracy
		self.description = description
		self.category = category
	
	def getName(self):
		"""Returns move name"""
		return self.name

	def getType(self):
		"""Returns move type"""
		return self.type

	def getPower(self):
		"""Returns move's power"""
		return self.power

	def getAccuracy(self):
		"""Return's move's accuracy"""
		return self.accuracy

	def getDescription(self):
		"""Returns move description"""
		return self.description

	def getCategory(self):
		"""Returns move category (special or physical"""
		return self.category
