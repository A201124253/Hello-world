#创建一系列对象

#子弹

class Bullet:
	def __init__(self, lethality):
		self.lethality = lethality
	
	def lethality(self):
		return self.lethality

#弹夹

class Clip:

	def __init__(self, capacity):
		self.clip_capacity = capacity
		self.bullet_list = []
	def bullet_in(self, bullet):
		self.bullet_list.append(bullet)
		print("压入了一颗子弹，当前子弹数量为%d"%len(self.bullet_list))
	def bullet_out(self):
		if len(self.bullet_list)>0:
			self.bullet_list[-1].lethality()
			self.bullet_list.pop()
			print("子弹-1...当前的子弹数是:%d"%len(self.bullet_list))
		else:
			lethality = 0
		return lethality
#枪

class Gun:

	def __init__(self, name):
		self.name = name
		self.clip = None
	def __str__(self):
		if self.clip:
			return "枪当前有弹夹"
		else:
			return "枪当前没有弹夹"

	def change_clip(self, clip):
		if not self.clip:
			self.clip = clip

	def shoot(self, aim):
		bullet = self.clip.bullet_out()
		if bullet:
			bullet.lethality()
		else:
			print("没有子弹了，放了空枪……")
#人
class People:
	
	def __init__(self, name):
		self.name = name
		self.life = 100
	
	def buy_gun(self, gun):
		self.gun = gun
		print(self.name+'买了一把'+self.gun.name)

	def bullet_into_clip(self, clip, bullet):
		clip.bullet_in(bullet)

	def clip_in(self, clip):
		self.gun.change_clip(clip)

	def shoot(self, aim):
		self.gun.shoot(aim)


	def lose_blood(self, lethality):
		self.life-=lethality
		print('剩余的生命值为%d'%self.life)


Peter = People ('Peter')

awm = Gun('awm')

Peter.buy_gun(awm)

#创建弹夹
clip = Clip(100)
#创建一颗子弹
bullet = Bullet(5)

Peter.bullet_into_clip(clip, bullet)

Peter.clip_in(clip)

John = People('John')

Peter.shoot(John)
