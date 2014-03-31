import random

biomes = ["forest","plains","desert","tundra","ocean","mountains","river","canal"]

class Tile(object):
	def __init__(self, tile_biome):
		if biomes[tile_biome] == "forest":
			self.available_food = 2	# The tile contains enough food to push the reserves up by two, every turn.
			self.trees = True		# The tile contains trees, which can be cut for wood.
			self.deer = True		# The tile contains deer, which can be made into vennisen.
			self.cattle = False		# The tile does not contain  cattle.
			self.pigs = False		# The tile does not contain pigs.
			self.fish = False		# The tile does not contain fish.
			self.fertile = False	# The tile cannot be farmed.
			self.owner = None
			
