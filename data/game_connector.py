from .states import level1
from .components import Agent
import pygame as pg
import datetime
from _thread import *
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
		self.jumping = False
		self.jumpTime = datetime.datetime.now().time().second
		self.thingDone = False
		

	def getEnemyPos(self):
		for enemy in self.level.enemies_group:
			if(enemy.rect.x != 0):
				if(enemy.rect.x - self.level.mario.rect.x < -20):
					self.level.enemies_group.remove(enemy)
				else:
					self.enemys = enemy.rect.x
					break
	def getPipePos(self):
		self.agent.pipe_list = self.level.pipe_list

	def getHolePos(self): #TODO: enter hole positions into agent
		for groundBit in self.level.ground_list:
			if((groundBit.rect.x + groundBit.width) != 0):
				self.agent.hole_list.append(groundBit.rect.x + groundBit.width)


	def getStepPos(self):
		self.agent.step_list = self.level.step_list


	#def makeMove(self):

	#	if self.agent.nextMove(self.level.mario.rect.x,self.enemys) == "right":
	#		return "right"
	#	else:
	#		self.jumping = True
	#		self.jumpTime = datetime.datetime.now().time().second
	#		try:
	#			thread.start_new_thread(self.jumpTime)
	#		except:
	#			print("NOOOOOOOO")
	#		return "jump" 


	def jumpTime(self):
		while(current - self.jumpTime) < 0.1:
			pass
		self.jumping = False
		l = list(tools.keys)
		l[keybinding["jump"]] = 0
		tools.keys = tuple(l)


	#def executeInput(self,tools):
	#	current = datetime.datetime.now().time().second
	#	if self.level.started:
	#		if self.thingDone == False:
	#			self.pipePos()
	#			self.getHole()
	#			self.getSteps()
	#			self.thingDone = True
	#		if self.jumping:
	#			if (current - self.jumpTime) > 0.1:
	#				self.jumping = False
	#				l = list(tools.keys)
	#				l[keybinding["jump"]] = 0
	#				tools.keys = tuple(l)
	#				
	#		else:
	#		    self.getEnemyPos()
	#		    l = list(tools.keys)
	#		    l[keybinding[self.makeMove()]] = 1
	#		    tools.keys = tuple(l)



	def executeInput(self,tools):
		if self.level.started:
			self.getEnemyPos()
			if self.thingDone == False:
				self.getPipePos()
				self.getHolePos()	
				self.getStepPos()
				self.thingDone = True
			action = self.agent.nextMove(self.level.mario.rect.x,self.enemys)
			current = datetime.datetime.now().second
			if self.jumping:
				if (current - self.jumpTime) > 0.3:
					self.jumping = False
					l = list(tools.keys)
					l[keybinding["jump"]] = 0
					tools.keys = tuple(l)
			else:
				if action == "jump":
					self.jumping = True
					self.jumpTime = datetime.datetime.now().second
				l = list(tools.keys)
				l[keybinding[action]] = 1
				tools.keys = tuple(l)
