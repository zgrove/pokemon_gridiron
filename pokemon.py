#!/usr/bin/env python3
from intro import intro
from choose1 import prebattle

rival_name = intro()
chosen_Pokemon = prebattle(rival_name)

print("Player: " + chosen_Pokemon[0].getName() + " " + str(chosen_Pokemon[0].getMove(3).getPower()))
