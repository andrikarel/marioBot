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
		self.groundY = 498
		self.maxJumpY = 162


	def posPrediction(self):
		pass



	def nextMove(self, enemies, mario):
		self.legalMoves = self.getLegalMoves()
		self.move = self.aStar()
		return "jump"

	def getLegalMoves(self):
		return 0

	def aStar(self):
		return 0



# if keys[tools.keybinding['jump']]:
#             if self.allow_jump:
#                 if self.big:
#                     #setup.SFX['big_jump'].play()
#                 else:
#                     #setup.SFX['small_jump'].play()
#                 self.state = c.JUMP
#                 if self.x_vel > 4.5 or self.x_vel < -4.5:
#                     self.y_vel = c.JUMP_VEL - .5
#                 else:
#                     self.y_vel = c.JUMP_VEL

# elif keys[tools.keybinding['right']]:
#             self.get_out_of_crouch()
#             self.facing_right = True
#             if self.x_vel < 0:
#                 self.frame_index = 5
#                 self.x_accel = c.SMALL_TURNAROUND
#             else:
#                 self.x_accel = c.WALK_ACCEL

#             if self.x_vel < self.max_x_vel:
#                 self.x_vel += self.x_accel
#                 if self.x_vel < 0.5:
#                     self.x_vel = 0.5
#             elif self.x_vel > self.max_x_vel:
#                 self.x_vel -= self.x_accel
