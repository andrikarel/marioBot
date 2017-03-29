


class PosState(object):
	def __init__(self, xStart, yStart, enemies_group):
		super(PosState, self, xStart, yStart).__init__()
		self.xStart = xStart
		self.yStart = yStart
		self.xEnd = xStart + 20
		self.yEnd = yStart + 20
		self.enemies_group = enemies_group


	def containsEnemy(self, enemies_group):
		for enemy in self.enemies_group:
			if enemy.rect.x > self.xStart and enemy.rect.x < self.xEnd and enemy.rect.y > self.yStart and enemy.rect.y < self.yEnd:
				return True
		return False

	def containsHole(self):
		for groundBit in self.level.ground_list:
			if(groundBit.rect.x + groundBit.width)

