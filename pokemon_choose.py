#!/usr/bin/env python3

from classes import *

SolarBeam = Move("Solar Beam", "Grass", 120, 100, " ", "Special")
SludgeBomb = Move("Sludge Bomb", "Poison", 90, 100, " ", "Special")
RazorLeaf = Move("Razor Leaf", "Grass", 70, 95, " ", "Physical")
DoubleEdge = Move("Double Edge", "Normal", 120, 100, " ", "Physical")

Venusaur_stats = Stats(164, 111, 112, 129, 129, 109)

Venusaur = Pokemon("Venusaur", "Grass", "Poison", [SolarBeam, SludgeBomb, RazorLeaf, DoubleEdge], Venusaur_stats)
#Blastoise = 
#Charizard = 
#Pikachu = 
#Dragonite = 
#Machamp = 

print(Venusaur.getMove(2).getName())
