import random
from . import mario

class Agent(object):
	"""docstring for Agent"""
	def __init__(self):
		super(Agent, self).__init__()


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


	def nextMove(self,marioPos,enemyPos,pipe,hole):
		if self.enemyNear(marioPos, enemyPos) or self.pipeNear(marioPos, pipe) or self.holeNear(marioPos, hole):
			return "jump"
		return "right"

	def enemyNear(self, marioPos, enemyPos):
		if enemyPos != 0 and (enemyPos - marioPos < 100) and (marioPos - enemyPos < 30):
			print("IT'S THE FUCKING ENEMY")
			return "jump"

	def pipeNear(self, marioPos, pipe):
		if pipe - marioPos < 35:
			print("IT'S THE FUCKING PIPE")
			return "jump"

	def holeNear(self, marioPos, hole):
		if hole != 0 and hole - marioPos < 10:
			print("IT'S THE FUCKING HOLE")
			return "jump"