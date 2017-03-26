import random
from . import mario

class Agent(object):
	"""docstring for Agent"""
	def __init__(self):
		super(Agent, self).__init__()


	def nextMove(self,marioPos,enemyPos,pipe):
		if enemyPos != 0:
			if ((enemyPos - marioPos < 100) and (marioPos - enemyPos < 30)):
				return "jump"
			elif (pipe - marioPos == 30):
				return "jump"
		elif (pipe - marioPos < 50):
			return "jump"
		return "right"