from .states import level1

class GameConnector(object):
	def __init__(self,level):
		self.level = level

	def printStuff(self):
		print(self.level.getFlagScore())