class State(object):
	def __init__(self, marioPosX, marioPosY, enemies_group, pipes,holes,stairs,depth):
		self.xStart = marioPosX
		self.yStart = marioPosY
		self.xEnd = self.xStart + 200
		self.yEnd = self.yStart + 200
		self.enemies_group = enemies_group
		self.pipes = pipes
		self.stairs = stairs
		self.holes = holes
		self.depth = depth


	def legalMoves(self):
		return ["right","jump"]

	def successorState(self, move):
		if move == "right":
			pipeDistance = self.nearestPipe()
			#holeDistance = self.nearestHole()
			stairDistance = self.nearestStair()
			if(pipeDistance > 125 and stairDistance > 30):
				return State(self.xStart+6, self.yStart, self.enemies_group,self.pipes,self.holes,self.stairs,self.depth + 1)
			else:
				return State(self.xStart,self.yStart,self.enemies_group,self.pipes,self.holes,self.stairs,self.depth + 1)
		if move == "jump":
			#er mariox + 150 jafnt og hola? y+++++++
			if (self.xStart+150) >= self.nearestHole():
				return State(self.xStart+6, self.yStart+25, self.enemies_group,self.pipes,self.holes,self.stairs,self.depth + 1)
			return State(self.xStart+6, self.yStart, self.enemies_group,self.pipes,self.holes,self.stairs,self.depth + 1)

		
	def isGoal(self):
		if self.xStart > 8505 or self.depth == 10:
			return True
		return False	

	def nearestPipe(self):
		for pip in self.pipes:
			if pip.rect.x > self.xStart:
				return pip.rect.x - self.xStart
		return Infinity


	def nearestHole(self):
		for groundBit in self.holes:
			if(groundBit > self.xStart):
				return groundBit - self.xStart
		return Infinity
	def nearestStair(self):
		for stair in self.stairs:
			if(stair.rect.x > self.xStart):
				return stair.rect.x - self.xStart
		return Infinity

