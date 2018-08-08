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

#1. 获取用户需求，定时还是加作料
def time_or_condi():
	print("\n\n\n")
	print("="*30)
	print("	非智能烤箱V1.0	")
	print("1.设定时间")
	print("2.添加作料")
	print("0.关闭烤箱")
	print("="*30)
	print("\n\n\n")


	key = int(input("请输入要进行的操作序号:"))
	return key
	
#2. 获取定时时间
def time():
	time = int(input("请设定定时器时间:"))
	red_sweet_patato.cook(time)
	print(red_sweet_patato)


#3. 获取添加的作料
def condiments():
	condiment = input("请加入调料:")
	red_sweet_patato.add_condiments(condiment)
	print(red_sweet_patato)

def main():
	while True:	
		key = time_or_condi()
		if key==1:
			#获取用户定时
			time()
		elif key==2:
			#获取需要添加的调料
			condiments()
		elif key==0:
			break	
red_sweet_patato = Sweet_patato()
main()
