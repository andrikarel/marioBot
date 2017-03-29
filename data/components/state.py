class State(object):
	def __init__(self, marioPosX, marioPosY, enemies_group, pipes):
		self.xStart = marioPosX
		self.yStart = marioPosY
		self.xEnd = xStart + 200
		self.yEnd = yStart + 200
		self.enemies_group = enemies_group
		self.pipes = pipes


	def legalMoves(self, enemies_group):
		return ["right","jump"]

	def successorState(self, move):
		if move == "right":
			distance = self.nearestPipe()
			if(distance > 6)
				return State(self.xStart+6, self.yStart, self.enemies_group,self.pipes)
			else:
				return State(self.xStart+distance,self.yStart,self.enemies_group,self.pipes)
		else:
			

	def nearestPipe(self):
		for pip in self.pipes:
			if pip.rect.x > self.xStart:
				return pip.rect.x - self.xStart
		return Infinity


	def containsHole(self):
		for groundBit in self.level.ground_list:
			if(groundBit.rect.x + groundBit.width)
