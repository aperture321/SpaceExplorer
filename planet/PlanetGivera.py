#! /usr/bin/env python

import sys, os, random

class Planet_Givera(object):
	def __init__(self):
		self.planetType = "Flat"
		self.planetAtmosphere = "Oxygen"
		self.hasLife = "True"
		self.fuelAssign()
		self.fueling = random.randint(1,400)


