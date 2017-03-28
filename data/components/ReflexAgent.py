import random
from . import mario

class ReflexAgent(object):
	"""docstring for Agent"""
	def __init__(self):
		super(ReflexAgent, self).__init__()
		self.pipe_list = []
		self.hole_list = []
		self.step_list = []

	def nextMove(self,marioPos,enemyPos):
		if self.enemyNear(marioPos, enemyPos) or self.pipeNear(marioPos) or self.holeNear(marioPos) or self.stepNear(marioPos):
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
			elif self.hole_list[0] - marioPos < 100:
				return True

	def stepNear(self, marioPos):
		if self.step_list:
			if self.step_list[0].rect.x - marioPos < 25:
				self.step_list.remove(self.step_list[0])
			elif self.step_list[0].rect.x - marioPos < 150:
				return True