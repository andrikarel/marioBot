from . import mario

class AStarAgent(object):
	"""docstring for Agent"""
	def __init__(self):
		super(AStarAgent, self).__init__()
		self.pipe_list = []
		self.hole_list = []
		self.step_list = []
		self.xPos = 0
		self.yPos = 0
		self.jumpIntensity = 0
		self.legalMoves = 0
		self.move = 0


	def posPrediction(self):
		pass



	def nextMove(self):
		self.legalMoves = self.getLegalMoves()
		self.move = self.aStar()
		return "right"

	def getLegalMoves(self):
		return 0

	def aStar(self):
		return 0