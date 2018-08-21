import time

class Person(object):
	"""人的类"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		self.gun = None #用来保存对枪的引用
		self.hp = 100

	def bullet_in(self, clip, bullet):
		'''把子弹装到弹夹中'''
		#弹夹，保存子弹
		clip.save_bullet(bullet)

	def clip_in(self, gun, clip):
		#枪， 安装弹夹
		gun.save_clip(clip)
	
	def pick_gun(self, gun):
		"""老王拿起一把枪"""
		self.gun = gun
	
	def shoot(self, enemy):
		#枪.开火（敌人）
		self.gun.fire(enemy)
	def lose_blut(self, lethality):
		self.hp -= lethality

	def __str__(self):
		if self.gun:
			return "%s的血量为:%d, 他有枪"%(self.name, self.hp)
		else:
			return "%s的血量为%d，他没枪"%(self.name, self.hp)

class Gun(object):
	"""枪类"""
	def __init__(self, name):
		super(Gun, self).__init__()
		#用来记录枪的类型
		self.name = name

	def save_clip(self, clip):
		self.clip = clip

	def __str__(self):
		if self.clip:
			return "枪的信息为:%s, %s"%(self.name, self.clip)
		else:
			return "枪的信息为:%s, 这把枪中没有弹夹"%(self.name)

	def fire(self,enemy):
		'''枪从弹夹中获取一发子弹，然后让这发子弹取击中敌人'''

		#先从弹夹中取子弹
		bullet_temp = self.clip.pop_bullet()
		
		#让这个子弹去伤害敌人
		if bullet_temp:
			bullet_temp.aimd(enemy)
		else:
			print("弹夹中没有子弹了……")

class Clip(object):#Danjia = Clip
	"""弹夹类"""
	def __init__(self, max_num):
		super(Clip, self).__init__()
		#用来弹夹最大容量
		self.max_num = max_num
		#用来记录所有子弹的引用
		self.bullet_list = []
	
	def __str__(self):
		return "弹夹状态为:%d/%d"%(len(self.bullet_list),self.max_num)

	def save_bullet(self, bullet):
		"""将这颗子弹保存"""
		self.bullet_list.append(bullet)
	
	def pop_bullet(self):
		if self.bullet_list:
			return self.bullet_list.pop()
		else:
			return None

class Bullet(object):
	#Zidan = Bullet
	"""子弹类"""
	def __init__(self, lethality):

		#shashangli = lethality
		super(Bullet, self).__init__()
		#用来记录子弹的杀伤力
		self.lethality = lethality
	
	def aimd(self, enemy):
		'''让敌人掉血'''
		enemy.lose_blut(self.lethality)

def main():
	"""用来控制整个程序的流程"""

	#1. 创建老王对象laowang = Peter
	Peter = Person ("Peter")

	#2. 创建一个枪对象
	ak47 = Gun("ak47")  

	#3. 创建一个弹夹对象
	clip_normal = Clip(20)
	
	#4. 创建一些子弹
	bullet = Bullet(10)

	#5. 老王把子弹安装到弹夹中
	'''
	#i = 0
	#while i<clip_normal.max_num:
	for i in range(clip_normal.max_num):
		Peter.bullet_in(clip_normal, bullet)
		time.sleep(1)
		str_clip_normal =str(clip_normal)
		print("正在装弹"+str_clip_normal[7:]+'['+'#'*(i+1)+' '*(clip_normal.max_num-i-1)+']')
		i+=1
	'''
	Peter.bullet_in(clip_normal, bullet)

	#6. 老王把弹夹安装到枪中
	#print("子弹已满，更换弹夹")
	
	Peter.clip_in(ak47, clip_normal)
	
	#test 测试弹夹的信息
	print(clip_normal)
	
	#test 测试枪的信息
	print(ak47)
	
	#7. 老王拿枪
	Peter.pick_gun(ak47)
	print(Peter)
	
	#8. 创建一个敌人 
	John = Person("John")
	print(John)

	#9. 老王开枪打敌人
	#老王扣扳机打老宋
	Peter.shoot(John)
	print(John)
if __name__ == '__main__':
	main()
