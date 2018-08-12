import time
class Gun:
	#属性
	color = '黑色'
	
	#方法
	def set_name(self, new_name):
		self.__name = new_name

	#用来设置枪的子弹数量
	def set_bullet_num(self, num):
		self.__bullet_num = num
	
	#定义一个方法，用来设置一个属性，这个属性用来表示，每次开枪射出去的子弹数
	def set_minus_bullet_num(self, num):
		self.__minus_bullet_num = num

	def shoot(self):
		self.__bullet_num -=self.__minus_bullet_num
		print("%s当前的子弹数量为:%d"%(self.__name, self.__bullet_num))

AK47 = Gun()
AK47.set_name('AK47')
AK47.set_bullet_num(100)
AK47.set_minus_bullet_num(2)

MP5 = Gun()
MP5.set_name('MP5')
MP5.set_bullet_num(80)
MP5.set_minus_bullet_num(2)

#设置完成，下面开始射击

AK47.shoot()
MP5.shoot()

time.sleep(5)

AK47.shoot()
MP5.shoot()



