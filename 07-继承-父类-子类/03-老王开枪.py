#创建一系列对象

#子弹

class Bullet:
	def __init__(self, lethality):
		self.lethality = lethality
#弹夹

class Clip:

	def __init__(self, capacity):
		self.clip_capacity = capacity
		self.bullet_list = []
	def recive_bullet(self, bullet):
		self.bullet_list.append(bullet)
		print("压入了一颗子弹，当前子弹数量为%d"%len(self.bullet_list))

#枪

class Gun:

	def __init__(self, name):
		self.name = name

#人
class People:
	
	def __init__(self, name):
		self.name = name
	
	def buy_gun(self, gun):
		self.gun = gun
		print(self.name+'买了一把'+self.gun.name)

	def bullet_into_clip(self, clip, bullet):
		pass
Peter = People ('Peter')

awm = Gun('awm')

Peter.buy_gun(awm)

#创建弹夹
clip = Clip(100)
#创建一颗子弹
bullet = Bullet(5)

Peter.bullet_into_clip(clip, bullet)

clip.recive_bullet(bullet)
