#! /usr/bin/env python

import random

class Planet_Ala(object):
	def __init__(self):
		self.planetType = "Rocky" #Planet type
		self.planetAtmosphere = "Oxygen" #Planet oxygen level
		self.hasLife = "False" #Life - "True" or "False"
		self.fueling = random.randint(1,400)
