#!/usr/bin/env python

import sys
import os

class battery():
	def __init__(self):
		self.batteryLevel = 100000
	def countdown(self):
		while self.batteryLevel != 0:
			continue ##TODO find where this happens!!!
	def pause(self):
		self.batteryLevel = self.batteryLevel
	def refill(self):
		self.batteryLevel += 10#TODO figure out refill level
