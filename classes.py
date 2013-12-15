#!/usr/bin/env python3

from enum import Enum

Type = Enum('Fire', 'Water', 'Grass', 'Electric', 'Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Psychic', 'Ice', 'Dragon', 'Steel', 'Dark', 'None')

class Stats(Object):
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

class Pokemon(Object):
	"""Describes a Pokemon"""
	
	def __init__(self, name, currentHp, faint):
		"""Init method for initializing Pokemon Class"""
		self.name = name
		self.currentHp = currentHp
		self.faint = faint

	def getName(self):
		"""Returns Pokemon's name"""
		return self.name

	def getCurrentHp(self):
		"""Returns Pokemon's current HP"""
		return self.currentHp

	def getFaint(self):
		"""Returns Pokemon's Faint status"""
		return self.faint
