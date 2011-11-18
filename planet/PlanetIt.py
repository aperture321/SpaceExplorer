#! /usr/bin/env python

import random

class Planet_It(object):
	def __init__(self):
		self.planetType = "Rocky"
		self.planetAtmosphere = "Oxygen"
		self.hasLife = "False"
		self.fueling = random.randint(1,400)
