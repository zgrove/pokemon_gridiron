#!/usr/bin/env python3

from classes import *

SolarBeam = Move("Solar Beam", "Grass", 120, 100, " ", "Special")
SludgeBomb = Move("Sludge Bomb", "Poison", 90, 100, " ", "Special")
RazorLeaf = Move("Razor Leaf", "Grass", 70, 95, " ", "Physical")
DoubleEdge = Move("Double Edge", "Normal", 120, 100, " ", "Physical")
FireBlast = Move("Fire Blast", "Fire", 120, 85, " ", "Special")
AirSlash = Move("Air Slash", "Flying", 75, 95, " ", "Special")
DragonPulse = Move("Dragon Pulse", "Dragon", 80, 100, " ", "Special")
HydroPump = Move("Hydro Pump", "Water", 120, 85, " ", "Special")
SkullBash = Move("Skull Bash", "Normal", 130, 100, " ", "Physical")
Blizzard = Move("Blizzard", "Ice", 120, 75, " ", "Special")
AuraSphere = Move("Aura Sphere", "Fighting", 90, 100, " ", "Special")
Thunder = Move("Thunder", "Electric", 110, 70, " ", "Special")
VoltTackle = Move("Volt Tackle", "Electric", 120, 100, " ", "Physical")
IronTail = Move("Iron Tail", "Steel", 100, 75, " ", "Physical")
QuickAttack = Move("Quick Attack", "Normal", 80, 100, " ", "Physical")
HyperBeam = Move("Hyper Beam", "Normal", 150, 90, " ", "Special")
IceBeam = Move("Ice Beam", "Ice", 90, 100, " ", "Special")
DragonClaw = Move("Dragon Claw", "Dragon", 80, 100, " ", "Physical")
Waterfall = Move("Waterfall", "Water", 80, 100, " ", "Physical")
CrossChop = Move("Cross Chop", "Fighting", 100, 80, " ", "Physical")
ThunderPunch = Move("Thunder Punch", "Electric", 75, 100, " ", "Physical")
IcePunch = Move("Ice Punch", "Ice", 75, 100, " ", "Physical")
Earthquake = Move("Earthquake", "Ground", 100, 100, " ", "Physical")

Venusaur_stats = Stats(187, 134, 135, 152, 152, 132)
Blastoise_stats = Stats(186, 135, 152, 137, 157, 130)
Charizard_stats = Stats(185, 136, 130, 161, 137, 152)
Pikachu_stats = Stats(167, 142, 107, 142, 132, 162)
Dragonite_stats = Stats(198, 186, 147, 152, 152, 132)
Machamp_stats = Stats(197, 182, 132, 117, 137, 107)

Venusaur = Pokemon("Venusaur", "Grass", "Poison", [SolarBeam, SludgeBomb, RazorLeaf, DoubleEdge], Venusaur_stats)
Blastoise = Pokemon("Blastoise", "Water", "None", [HydroPump, SkullBash, Blizzard, AuraSphere], Blastoise_stats)
Charizard = Pokemon("Charizard", "Fire", "Flying", [FireBlast, AirSlash, DragonPulse, SolarBeam], Charizard_stats)
Pikachu = Pokemon("Pikachu", "Electric", "None", [Thunder, VoltTackle, IronTail, QuickAttack], Pikachu_stats)
Dragonite = Pokemon("Dragonite", "Dragon", "Flying", [HyperBeam, IceBeam, DragonClaw, Waterfall], Dragonite_stats)
Machamp = Pokemon("Machamp", "Fighting", "None", [CrossChop, ThunderPunch, IcePunch, Earthquake], Machamp_stats)


pokeList = {"Venusaur": Venusaur, "Blastoise": Blastoise, "Charizard": Charizard, "Pikachu": Pikachu, "Dragonite": Dragonite, "Machamp": Machamp}
