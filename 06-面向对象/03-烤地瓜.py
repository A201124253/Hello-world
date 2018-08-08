class Sweet_patato:
	
	#用来完成一些初始化的工作
	def __init__(self):
		self.cooked_level = 0
		self.cooked_string = "生的"
		self.condiments = []
	def __str__(self):
		msg = "地瓜的生熟程度为:" + self.cooked_string + "\t" 
		msg += " 等级为:" + str(self.cooked_level) + "\t"
		if len(self.condiments)>0:
			msg += "已经添加的作料为:" #作料为：芥末酱，番茄酱，酱油，孜然
			
			for condiment in self.condiments:
				
				msg += condiment + ","
			#去掉逗号，方法一
			#msg.strip(",")
			#方法二
			msg = msg[:-1]
		else:
			msg+="当前没有添加作料"
		return msg
	def cook(self, times):
		self.cooked_level += times
		if self.cooked_level>8:
			self.cooked_string = "焦了"
		elif self.cooked_level>5: 
			self.cooked_string = "熟了"
		elif self.cooked_level>3:
			self.cooked_string = "半生不熟"
		else:	
			self.cooked_string = "生的"
	#添加作料
	def add_condiments(self, temp):
		self.condiments.append(temp)

red_sweet_patato = Sweet_patato()
print(red_sweet_patato)

red_sweet_patato.cook(2)
print(red_sweet_patato)

red_sweet_patato.add_condiments("芥末酱")
print(red_sweet_patato)
red_sweet_patato.add_condiments("孜然")
print(red_sweet_patato)

red_sweet_patato.cook(2)
print(red_sweet_patato)

red_sweet_patato.add_condiments("花生酱")
print(red_sweet_patato)

red_sweet_patato.cook(3)
print(red_sweet_patato)

red_sweet_patato.add_condiments("芝麻酱")
print(red_sweet_patato)

