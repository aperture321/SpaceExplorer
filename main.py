#! /usr/bin/env python
"""SpaceExplorer v1.0"""
#Standard imports.
import sys
import os
import time
import thread

#Planets imports
import planet
import planet.PlanetAla
import planet.PlanetIt
import planet.PlanetGivera

import useful.battery
import useful.lifesupport

class Universe(object):
	def __init__(self):
		self.batLevel = 100
		self.startedUp = "False"
		self.shipStarted = "False"
		self.planets = ["Ala", "Givera", "It"]
		self.exit = "False"
		self.planetAla = planet.PlanetAla.Planet_Ala()
		self.planetIt = planet.PlanetIt.Planet_It()
		self.planetGivera = planet.PlanetGivera.Planet_Givera()
		self.lifeSupport = useful.lifesupport.LifeSupport()
		self.battery = useful.battery.battery()
		self.docked = "False"
		self.lifesupport_started = "False"
		while True:
			if self.exit == "True":
				exit()
			else:
				self.mprint()

	def mprint(self):
		exitRetries = 0 # defines
		while self.exit == "False":
			planets = "Ala", "Givera"
			if self.startedUp != "True":
				#print "\033[34mThis is blue\033[0m" - Color test
				print "\033[31mGMS-OPPERTUNITY - MAINFRAME\033[0m"
				self.startedUp = "True"
			cmd = raw_input().split(" ")
			#Debugging code
			if len(sys.argv) >= 2:
				if sys.argv[1] == '-d':
					print len(cmd)
			if cmd[0] == "START":
				self.START()
			elif cmd[0] == "HELP":
				self.HELP()
			elif cmd[0] == "GOTO":
				self.GOTO(cmd)	
			elif cmd[0] == "BATTLEVEL":
				print "%s%s" % (self.batLevel, "%")
			elif cmd[0] == "SHUTDOWN":
				self.SHUTDOWN()
			elif cmd[0] == "PLANETCHOICE":
				self.PLANETCHOICE()
			elif cmd[0] == "PLANETPROPS":
				self.getPlanetProperties(self.currentPlanet)
			else:
				if self.exit == "False":
					print "\033[31mCOMMAND NOT VALID"
					print "try typing HELP\033[0m"
					exitRetries = exitRetries - 1
					if exitRetries <= -5:
						print "\033[1;31mSHUTTING DOWN\033[0m"
						self.exit = "True"

	def START(self):
		print "\033[1;34mBATTLEVEL = %s%s\033[0m" % (self.batLevel, "%")
	        if self.batLevel <= 10 or self.shipStarted == "True":
                        print "STARTUP NOT VALID"
                else:
                        print "\033[0;34mINITIATING STARTUP SEQUENCE\033[0m"
                        print "\033[0;34mSTARTING UP GENERATORS\033[0m"
                        print "\033[0;34mATTEMTPING TO STARTUP REMOTE CONNECTION\033[0m... DONE"
                        print "\033[0;34mSTARTUP SUCCESSFUL.\033[0m"
                        self.batLevel = self.batLevel - (self.batLevel - (self.batLevel / 2))
                        print "\033[0;34mBATTLEVEL IS NOW %s%s\033[0m" % (self.batLevel, "%")
                        self.shipStarted = "True"
                        self.currentPlanet = "Ala"
                        thread.start_new_thread(self.battIncrease,(),)
			thread.start_new_thread(self.useO2,(),)

	def HELP(self):
		print "\033[0;34mOPTIONS:\nSTART\nHELP\nGOTO\nBATTLEVEL\nPLANETCHOICE\nSHUTDOWN\nPLANETPROPS\n\033[0m"

	def GOTO(self, cmd):
        	if self.shipStarted == "True":
                        if len(cmd) == 2:
					if cmd[1] != self.currentPlanet:
						if self.batLevel >= 10:
							if (self.batLevel - 20) >= 0:
								if cmd[1] in self.planets:
									print "\033[0;32mWARPING TO %s\033[0m" % cmd[1]
                                                                	time.sleep(2)
                                                        	        print "\033[0;32mARRIVED AT %s\033[0m" % cmd[1]
                                                        	        self.batLevel = self.batLevel - 20
                                                        	        self.currentPlanet = cmd[1]
								else:
									try:
										importModuleName = 'planets.Planet%s' % cmd[1]
										__import__(importModuleName)
										print "\033[0;32mRE-TRY JUMP\033[0m"
										self.planets.append("%s" % cmd[1])
										print self.planets
									except ImportError:
										print "\033[0;31mNO SUCH PLANET - CANNOT FIND PLANET FILE\033[0m"	
							else:
                                                                print "\033[0;31mBATTERY WOULD BE TOO LOW\033[0m"
						else:
        	                                        print "\033[0;31mBATTERY LEVEL TOO LOW\033[0m"
                			else:        
		                        	print "\033[0;32mYOU ARE ALREADY AT %s\033[0m" % cmd[1]
			else:
				print "\033[0;31mPLEASE SPECIFY A PLANET\033[0m"
		else:
                        print "\033[0;31mNOT STARTED UP\033[0m"

	def battIncrease(self):
		while self.shipStarted == "True":
			while self.batLevel <= 100:
				self.batLevel = self.batLevel + 1
				time.sleep(60)
	
	def PLANETCHOICE(self):
		print "\033[0;32mPLANETS:\033[0m"
		for i in self.planets:
			print "\033[0;32m" + i + "\033[0m"

	def getPlanetProperties(self, planet):
		try:
			print "\033[0;32mPlanet %s is a %s planet.\033[0m" % (planet, getattr(self, 'planet' + planet).planetType)
			if getattr(self, 'planet' + planet).hasLife == "True":
				print "\033[0;32mPlanet %s has life.\033[0m" % planet
			elif getattr(self, 'planet' + planet).hasLife == "False":
				print "\033[0;31mPlanet doesn't have life.\033[0m"
		except AttributeError:
			print "\033[0;31mERROR: Either planet has no planet file or there is no entry for planet %s.\033[0m" % planet	

	def SHUTDOWN(self):
		if self.shipStarted == "True":
			print "\033[0;31mSHUTTING DOWN SYSTEM\033[0m"
			self.exit = "True"
		else:
			print "\033[0;31mSYSTEM NOT STARTED; NO SHUTDOWN\033[0m"

	def useO2(self):
		while self.exit == "False":
			if self.lifesupport_started == "False":
				lifeSupport_O2Level = self.lifeSupport.O2Level
			if lifeSupport_O2Level <= 1:
				print "\033[0;31mO2 RAN OUT.\033[0m"
				self.exit = "True"
				return False
			time.sleep(1)
			self.lifesupport_started = "True"
			lifeSupport_O2Level = (lifeSupport_O2Level - 1)
			print lifeSupport_O2Level

universe = Universe()
universe.mprint()
