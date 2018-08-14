class Persen(object):
	"""人的类"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name

	def bullet_in(self, clip, bullet):
		'''把子弹装到弹夹中'''
		#弹夹，保存子弹
		clip.save_bullet(bullet)

	def clip_in(self, gun, clip):
		#枪， 安装弹夹
		gun.save_clip(clip)

class Gun(object):
	"""枪类"""
	def __init__(self, name):
		super(Gun, self).__init__()
		#用来记录枪的类型
		self.name = name

	def save_clip(clip):
		self.clip = clip

class Clip(object):#Danjia = Clip
	"""弹夹类"""
	def __init__(self, max_num):
		super(Clip, self).__init__()
		#用来弹夹最大容量
		self.max_num = max_num
		#用来记录所有子弹的引用
		self.bullet_list = []

	def save_bullet(self, bullet):
		"""将这颗子弹保存"""
		self.bullet_list += bullet


class Bullet(object):#Zidan = Bullet
	"""弹夹类"""
	def __init__(self, lethality):#shashangli = lethality
		super(Bullet, self).__init__()
		#用来记录子弹的杀伤力
		self.lethality = lethality

def main():
	"""用来控制整个程序的流程"""

	#1. 创建老王对象laowang = Peter
	Peter =Person ("Peter")

	#2. 创建一个枪对象
	ak47 = Gun("ak47")	

	#3. 创建一个弹夹对象
	clip_normal = Clip(20)
	
	#4. 创建一些子弹
	bullet = Bullet(10)

	#5. 老王把子弹安装到弹夹中
	Peter.bullet_in(clip_normal, bullet)

	#6. 老王把弹夹安装到枪中
	Peter.clip_in(ak47, clip_normal)

	#7. 老王拿枪

	#8. 创建一个敌人 

	#9. 老王开枪打敌人

if __name__ == '__main__':
	main()
