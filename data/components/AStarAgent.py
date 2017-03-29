from . import mario
from simpleai.search import SearchProblem, astar
from . import state
from .. import constants as c
class AStarAgent(object):
	"""docstring for Agent"""
	class HelloProblem(SearchProblem):
		def actions(self, state):
			return state.legalMoves()
		def result(self, state, action):
			return state.successorState(action)
		def is_goal(self, state):
			return state.isGoal()
		def heuristic(self, state):
			if state.yStart > c.GROUND_HEIGHT:
				return 500000
			return 8550-state.xStart
	def __init__(self):
		super(AStarAgent, self).__init__()
		self.pipe_list = []
		self.hole_list = []
		self.step_list = []
		self.jumpIntensity = 0
		self.move = 0
		self.groundY = 498
		self.maxJumpY = 162

	def posPrediction(self):
		pass

	def nextMove(self, enemies, mario):
		problem = self.HelloProblem(initial_state=state.State(mario.rect.x, mario.rect.y, enemies, self.pipe_list,self.hole_list,self.step_list,0))
		result = astar(problem)
		self.move = result.path()[1][0]
		return self.move

	def aStar(self):
		return 0

	def goalState(self, state):
		return False









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
