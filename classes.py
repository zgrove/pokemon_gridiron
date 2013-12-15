#!/usr/bin/env python3

class Stats(object):
	"""Constructs a class for the Pokemon's stats"""

	def __init__(self, hp, attack, defense, spAttack, spDefense, speed):
		"""Init method for initializing Stats class"""
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
