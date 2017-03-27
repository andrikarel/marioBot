import random
from . import mario

class Agent(object):
	"""docstring for Agent"""
	def __init__(self):
		super(Agent, self).__init__()
		self.pipe_list = []
		self.hole_list = []


	#def nextMove(self,marioPos,enemyPos,pipe,hole):
	#	if enemyPos != 0:
	#		if ((enemyPos - marioPos < 100) and (marioPos - enemyPos < 30)):
	#			return "jump"
	#		elif (pipe - marioPos == 30):
	#			return "jump"
	#		elif (hole - marioPos < 10):
	#			return "jump"
	#	elif (pipe - marioPos < 50):
	#		return "jump"
	#	elif (pipe - marioPos < 10):
	#		return "jump"
	#	return "right"


	def nextMove(self,marioPos,enemyPos):
		if self.enemyNear(marioPos, enemyPos) or self.pipeNear(marioPos) or self.holeNear(marioPos):
			return "jump"
		return "right"

	def enemyNear(self, marioPos, enemyPos):
		if enemyPos != 0 and (enemyPos - marioPos < 150) and (marioPos - enemyPos < 30):
			return True

	def pipeNear(self, marioPos):
		if self.pipe_list:
			if self.pipe_list[0].rect.x - marioPos < 25:
				self.pipe_list.remove(self.pipe_list[0])
			elif self.pipe_list[0].rect.x - marioPos < 150:
				return True


	def holeNear(self, marioPos):
		if self.hole_list:
			if self.hole_list[0] - marioPos < 30:
				self.hole_list.remove(self.hole_list[0])
			elif self.hole_list[0] - marioPos < 150:
				return True