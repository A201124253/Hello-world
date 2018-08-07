#定义一个猫类
class Cat:
	#属性
	def __init__(self, color, weight, teil):
		self.color = color
		self.weight = weight 
		self.teil = teil
		
	#方法
	def eat(self):
		print("-----吃------")
	def drink(self):
		print("-----喝------")
	def la(self):
		print("-----拉------")
	def sa(self):
		print("-----撒------")

	def print_info(self):
		print(self.color)
		print(self.weight)
		print(self.teil)
#创建一个猫对象
little_cat = Cat("花色", 5, "有")
'''
little_cat.eat()
little_cat.drink()
little_cat.la()
little_cat.sa()

#给little_cat对象添加属性
little_cat.color = "花色"
little_cat.weight = 5 #kg
little_cat.teil = "有"
#获取little_cat对象的属性
a = little_cat.color
print(a)
'''
little_cat.print_info()
