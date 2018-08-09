class Home:
	def __init__(self, area):
		self.area = area
		self.contains_item = []
	def __str__(self):
		msg = "家当前可用面积为："+str(self.area)
		msg += '\n'
		msg += "家里的物品有："
		
		return msg
	
	def add_item(self,item):
		if self.area>item.area:
			self.area-=item.area
			self.contains_item.append(item)

class Bed:
	def __init__(self, name, area):
		self.name = name
		self.area =area
	
	def __str__(self):
		msg = self.name + "床的面积为" + str(self.area)
		return msg
#创建一个家对象
home = Home(128)
print(home)

bed = Bed("席梦思", 4)
print(bed)

home.add_item(bed)
