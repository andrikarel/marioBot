from .states import level1
from .components import ReflexAgent
from .components import AStarAgent
import pygame as pg
import datetime
keybinding = {
    'action':pg.K_s,
    'jump':pg.K_a,
    'left':pg.K_LEFT,
    'right':pg.K_RIGHT,
    'down':pg.K_DOWN
}

class GameConnector(object):
	def __init__(self,level):
		self.level = level
		self.agent = AStarAgent.AStarAgent()
		self.enemys = []
		self.jumping = False
		self.jumpCounter = 0
		self.hazardsLogged = False
		

	def getEnemyPos(self):
		self.enemys = self.level.enemies_group
	def getPipePos(self):
		self.agent.pipe_list = self.level.pipe_list

	def getHolePos(self):
		for groundBit in self.level.ground_list:
			if((groundBit.rect.x + groundBit.width) != 0):
				self.agent.hole_list.append(groundBit.rect.x + groundBit.width)


	def getStepPos(self):
		self.agent.step_list = self.level.step_list

	def executeInput(self,tools):
		if self.level.started:
			self.getEnemyPos()
			if self.hazardsLogged == False:
				self.getPipePos()
				self.getHolePos()	
				self.getStepPos()
				self.hazardsLogged = True
			action = self.agent.nextMove(self.enemys, self.level.mario)
			if self.jumping:
				if self.jumpCounter >= 25:
					self.jumping = False
					l = list(tools.keys)
					l[keybinding["jump"]] = 0
					tools.keys = tuple(l)
					return
				else:
					self.jumpCounter +=1
					return
			if action == "jump":
				if not self.jumping:
					self.jumping = True
					self.jumpCounter = 0
			if action == 0:
				return
			l = list(tools.keys)
			l[keybinding[action]] = 1
			tools.keys = tuple(l)
