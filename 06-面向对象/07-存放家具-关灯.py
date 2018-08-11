class Home:
	def __init__(self, area):
		self.area = area
		self.light = "on"
		self.contains_item = []
						
	def __str__(self):
		msg = "家当前可用面积为："+str(self.area)
		msg += '\t'
		#列举家具
		if len(self.contains_item)>0:
			msg += "家里的物品有："
			for temp in self.contains_item:
				msg +=temp.get_name()+ ","
		
			msg = msg[:-1]
		
		else:
			msg += "家徒四壁"
	
		#显示灯的状态
		if self.light == "on":
			msg += "\t"+"当前灯是开着的，所有物品可见"
		else:
			msg += "\t"+"当前灯是关着的，一片漆黑"
		return msg

	def add_item(self,item):
		area = item.get_area()
		if self.area>area:
			self.area-=area
			self.contains_item.append(item)
	#修改所有对象的可见度
	def turn_on(self):
		self.light = "on"
		for temp in self.contains_item:
			temp.turnon()

	def turn_off(self):
		self.light = "off"
		for temp in self.contains_item:
			temp.turnoff()
		
		
class Bed:
	def __init__(self, name, area):
		self.name = name
		self.area =area
		self.light = "on"
	def __str__(self):
		msg  = self.name + "床的面积为："
		msg += str(self.area)+"\t" 
		msg += self.name + "的可见度为"
		msg += self.light
		return msg

	def get_name(self):
		return self.name
	
	def get_area(self):
		return self.area
	
	def turnon():
		self.light = "on"

	def turnoff(self):
		self.light = "off"

#创建一个家对象
home = Home(128)
print(home)

bed = Bed("席梦思", 4)
print(bed)

home.add_item(bed)
print(home)

bed2 = Bed("硬板床", 3)
print(bed2)

home.add_item(bed2)
print(home)

home.turn_off()
print(home)
print(bed)
print(bed2)
