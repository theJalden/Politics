import random
from nation import Nation

pope_names = ["Benedict", "Peter", "Linus", "Anacletus", "Clement", "Evaristus", "Urban", "Cornelius", "Lucius", "Stephen", "Innocent"]
senator_names = ["McCarthy", "Baner", "Feinstein", "Udall", "Bennet", "Blumenthal", "Murphy", "Carper", "Coons",  "Nelson", "Rubio"]
general_names = ["Sun Tzu", "Ghengis Khan", "Napoleon", "Caesar", "Pompey", "Leonidas", "Alexander", "Washington", "Custer", "Lee", "Grant"]
aristocrat_names = ["Louis", "Charles", "Robert", "Rudolph", "Hugh", "Philip", "John", "Clovis", "Charlemagne", "Francis", "Henry"]
class Politician(object):
	def __init__(self, title):
		self.title = title
		self.opinion = [0] * 7							#Dictate the opinions and prejudices of the politicians.
		if title == "pope":
			self.opinion[0] = random.randint(-10,5)		#Opinion 0 is Conservative/Liberal Negative numbers are more conservative, positive, more liberal.
			self.opinion[1] = random.randint(-10,10)	#Opinion 1 is Militarism. Negative numbers are pacifistic, positive are militaristic.
			self.opinion[2] = random.randint(60,100)	#Opinion 2 is Age.
			self.opinion[3] = 3							#Opinion 3 is economic views.
														#Opinion 3.1 is Capitalism.
														#Opinion 3.2 is Socialism.
														#Opinion 3.3 is Mercantilism
			self.opinion[4] = random.randint(1,3)		#Opinion 4 is Racial views. They range from 1-4, 1 being 100% tolerant, 4 being 100% racist.
			self.opinion[5] = random.randint(5,10)		#Opinion 5 is Social background. -10 is abject poverty, 10 is a life of luxury.
			self.opinion[6] = 1							#Opinion 6 is gender. 1 for male, 2 for female.
			self.name = pope_names[random.randint(0,10)
		elif title == "senator":
			self.opinion[0] = random.randint(-10,10)
			self.opinion[1] = random.randint(-10,10)
			self.opinion[2] = random.randint(35,100)
			self.opinion[3] = random.randint(1,4)
			self.opinion[4] = random.randint(1,3)
			self.opinion[5] = random.randint(0,10)
			self.opinion[6] = random.randint(1,2)
			self.name = senator_names[random.randint(0,10)]
		elif title == "general":
			self.opinion[0] = None
			self.opinion[1] = random.randint(7,10)
			self.opinion[2] = random.randint(30,100)
			self.opinion[3] = None
			self.opinion[4] = random.randint(1,3)
			self.opinion[5] = random.randint(-10,10)
			self.opinion[6] = random.randint(1,2)
			self.name = general_names[random.randint(0,10)]
		elif title == "aristocrat":
			self.opinion[0] = random.randint(-3,0)
			self.opinion[1] = random.randint(0,10)
			self.opinion[2] = random.randint(20,100)
			self.opinion[3] = 3
			self.opinion[4] = random.randint(1,3)
			self.opinion[5] = 10
			if random.randint(1,100)%20 == 0:
				self.opinion[6] = 2
			else:
				self.opinion[6] = 1
			self.name = aristocrat_names[0,10]
