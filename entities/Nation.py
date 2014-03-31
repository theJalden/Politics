import random
from politician import Politician



class Nation(object):
	def __init__(self, government, name):
		self.government = government
		self.name = name
		
		if self.government == "monarchy":
			self.conflicting = True 		# Shows that there will be some conflict for the leader of this nation. In this case, the pope.
			self.pope = Politician("pope") 	# Spawns a pope that can oppose the king.
			self.happiness = 3				# Sets the base amount of happiness for that type of government.
			self.population = 200
			self.food_reserves = 24
		if self.government == "oligarchy"
			self.conflicting = True
			self.aristocrats = [Politician("aristocrat")] * 7
			self.happiness = 2
			self.population = 200
			self.food_reserves = 24
		if self.government == "republic":
			self.conflicting = True
			self.senators = [Politician("senator")] * 200
			self.happiness = 5
			self.population = 200
			self.food_reserves = 24
