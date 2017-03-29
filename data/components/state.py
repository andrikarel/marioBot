class State(object):
	def __init__(self, marioPosX, marioPosY, enemies_group, obstacles):
		self.xStart = marioPosX
		self.yStart = marioPosY
		self.xEnd = xStart + 200
		self.yEnd = yStart + 200
		self.enemies_group = enemies_group
		self.obstacles = obstacles


	def legalMoves(self, enemies_group):
		return ["right","jump"]

	def successorState(self, move):
		if move == "right":
			if(self.wayIsClear())
				return State(self.xStart+6, self.yStart)

	def containsHole(self):
		for groundBit in self.level.ground_list:
			if(groundBit.rect.x + groundBit.width)
