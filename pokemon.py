#!/usr/bin/env python3
from intro import intro
from choose1 import prebattle
from battle import *

rival_name = intro()

answer = 'y'
while (answer == 'y'):
	chosen_Pokemon = prebattle(rival_name)
	battle([chosen_Pokemon[0]], rival_name, [chosen_Pokemon[1]])
	answer = input("\nWould you like to battle again? ('y' or 'n') ")
	while (answer != 'n' and answer != 'y'):
		answer = input("That's not a valid answer. Would you like to battle again? ('y' or 'n') ")

print("\nThanks for playing!")
