#1.打印功能提示
print("="*50)
print("	名字管理系统 V8.6")
print("	1:添加一个新的名字")
print("	2:删除一个名字")
print("	3:修改一个名字")
print("	4:查询一个名字")
print("	5:退出系统")
print("="*50)

names = []#定义一个空的列表来存储你添加的名字
while 1:
		num = int(input("请输入功能序号:"))
	
		#3.根据用户的选择，执行相应的功能
		if num==1:
			new_name = input("请输入一个名字:")
			names.append(new_name)
			print(names)
		elif num==2:
			remove_name = input("请输入一个名字:")
			if remove_name in names:
				names.remove(remove_name)
				print("%s已删除"%remove_name)
				print(names)
			else:
				print("这个名字本来就没有")
		elif num==3:
			#while 1:
					change_name = input("请输入要修改的名字:")
					if change_name in names:
						new_name = input("请输入新名字:")
						names[names.index(change_name)] = new_name
						#找到在列表中的位置并且替换
						print("已修改")
						print(names)
			#			break
					else:
						print("需要修改的名字不存在")
		elif num==4:
			find_name = input("请输入你要查询的名字")
			if find_name in names:
				print("找到了")
			else:
				print("查无此人")
		elif num==5:
			break
		else:
			print("您的输入有误，请重新输入")
