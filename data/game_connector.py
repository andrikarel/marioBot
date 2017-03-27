from .states import level1
from .components import Agent
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
		self.agent = Agent.Agent()
		self.enemys = 0
		self.pipes = 0
		self.hole = 0
		self.jumping = False
		self.jumpTime = datetime.datetime.now().time().second
		

	def getEnemyPos(self):
		for enemy in self.level.enemies_group:
			if(enemy.rect.x != 0):
				if(enemy.rect.x - self.level.mario.rect.x < -20):
					self.level.enemies_group.remove(enemy)
				else:
					self.enemys = enemy.rect.x
					break
	def pipePos(self):
		for pipe in self.level.pipe_list:
			if(pipe.rect.x != 0):
				if(pipe.rect.x - self.level.mario.rect.x < -20):
					self.level.pipe_list.remove(pipe)
				else:

					self.pipes = pipe.rect.x
					break

	def getHole(self):
		for groundBit in self.level.ground_list:
			if((groundBit.x + groundBit.width) != 0):
				self.hole = (groundBit.x + groundBit.width)
				print(self.hole)
				break


	def makeMove(self):

		if self.agent.nextMove(self.level.mario.rect.x,self.enemys,self.pipes,self.hole) == "right":
			return "right"
		else:
			self.jumping = True
			self.jumpTime = datetime.datetime.now().time().second

			return "jump" 


	def executeInput(self,tools):
		current = datetime.datetime.now().time().second
		if self.level.started:
			if self.jumping:
				if (current - self.jumpTime) > 0.1:
					self.jumping = False
					l = list(tools.keys)
					l[keybinding["jump"]] = 0
					tools.keys = tuple(l)
					
			else:
			    self.getEnemyPos()
			    self.pipePos()
			    l = list(tools.keys)
			    l[keybinding[self.makeMove()]] = 1
			    tools.keys = tuple(l)
