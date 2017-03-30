from .. import constants as c

class State(object):
	def __init__(self, marioPosX, marioPosY, marioVelY,marioState,enemies_group, pipes,holes,stairs,depth):
		self.xStart = marioPosX
		self.yStart = marioPosY
		self.xEnd = self.xStart + 200
		self.yEnd = self.yStart + 200
		self.marioVelY = marioVelY
		self.marioState = marioState
		self.enemies_group = enemies_group
		self.pipes = pipes
		self.stairs = stairs
		self.holes = holes
		self.depth = depth



	def legalMoves(self):
		if self.marioState == c.JUMP or self.marioState == c.FALL:
			return["right"]
		return ["right","jump"]


	def successorState(self, move):
		if ((self.marioState == c.JUMP or self.marioState == c.FALL) and self.marioVelY < c.MAX_Y_VEL):#Líklega villa
			self.marioVelY += c.JUMP_GRAVITY
		else:
			self.marioVelY = 0
			self.marioState = c.STAND

		nearestObstacle = self.nearestObstacle()
		
		if move == "right":
			nearestHole = self.nearestHole()
			if((self.marioState != c.JUMP) and self.xStart > nearestHole and self.xStart < (nearestHole + 50)):
				if(self.marioState == c.FALL):
					self.marioVelY = 10000
				self.marioVelY -= c.JUMP_VEL*0.8
				self.marioState = c.FALL
			if(not nearestObstacle or nearestObstacle.rect.x - self.xStart > 35 or self.yStart < nearestObstacle.rect.y):
				return State(self.xStart+6, self.yStart+self.marioVelY,self.marioVelY, self.marioState,self.enemies_group,self.pipes,self.holes,self.stairs,self.depth + 1)
			else:
				return State(self.xStart,self.yStart+self.marioVelY,self.marioVelY, self.marioState,self.enemies_group,self.pipes,self.holes,self.stairs,self.depth + 1)
		if move == "jump":
			if not (self.marioState == c.JUMP or self.marioState == c.FALL):
				self.marioState = c.JUMP
				self.marioVelY = c.JUMP_VEL
			if(not nearestObstacle or nearestObstacle.rect.x - self.xStart > 35 or self.yStart < nearestObstacle.rect.y):
				return State(self.xStart+6, self.yStart+self.marioVelY,self.marioVelY, self.marioState,self.enemies_group,self.pipes,self.holes,self.stairs,self.depth + 1)
			else:
				return State(self.xStart,self.yStart+self.marioVelY,self.marioVelY, self.marioState,self.enemies_group,self.pipes,self.holes,self.stairs,self.depth + 1)
		

	def isGoal(self):
		if self.xStart >= 9000 or self.depth == 50:
			return True
		return False	

	def nearestObstacle(self):
		for pip in self.pipes:
			if pip.rect.x > self.xStart:
				nearestPipe = pip
				break
		else:
			nearestPipe = 0

		for stair in self.stairs:
			if stair.rect.x > self.xStart:
				nearestStair = stair
				break
		else:
			nearestStair = 0

		if nearestStair and nearestPipe:
			if nearestPipe.rect.x < nearestStair.rect.x:
				return nearestPipe
			else:
				return nearestStair
		elif nearestStair:
			return nearestStair
		elif nearestPipe:
			return nearestPipe
		else:
			return 0


	def nearestHole(self):
		for groundBit in self.holes:
			if(groundBit > self.xStart):
				return groundBit-50
		return 500000

