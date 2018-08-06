def print_menu():
	#1.打印功能提示
	print("="*30)
	print("	学生管理系统v1.o")
	print("1. 添加学生信息")
	print("2. 删除学生信息")
	print("3. 修改学生信息")
	print("4. 查询学生信息")
	print("5. 显示所有学生信息")
	print("0. 退出系统")
	print("="*30)
#用来保存学生数据
stu_infos = []
while True:
	#1.打印功能提示
	print_menu()

	#获取功能的选择
	key = input("请输入功能对应的数字: ")

	#根据用户的选择，进行相应的操作
	if key=="1":
		#1添加学生信息
		
		#1.1 提示并获取学生的姓名
		new_name = input("请输入新学生的名字：")

		#1.2 提示并获取学生的性别
		new_sex = input("请输入新学生的性别：（男/女）")
		
		#1.3 提示并获取学生的手机号
		new_phone = input("请输入新学生的手机号码：")
		
		new_info = {}
		new_info['name'] = new_name
		new_info['sex'] = new_sex
		new_info['phone'] = new_phone

		stu_infos.append(new_info)
	elif key=='3':
		pass
		#修改学生的信息
		#3.1 提示并获取需要修改的学生序号
		stu_ID =int(input("请输入要修改的学生的序号："))

		#3.2 重新输入学生的信息（姓名，性别，手机号码）
		#3.1.1 提示并获取学生的姓名
		new_name = input("请输入新学生的名字：")

		#3.1.2 提示并获取学生的性别
		new_sex = input("请输入新学生的性别：（男/女）")
		
		#3.1.3 提示并获取学生的手机号
		new_phone = input("请输入新学生的手机号码：")
		
		stu_infos[stu_ID-1]['name'] = new_name
		stu_infos[stu_ID-1]['sex'] = new_sex
		stu_infos[stu_ID-1]['phone'] = new_phone

	elif key=='5':
	#	print(stu_infos)
		print("="*30)
		print("学生的信息如下：")
		print("="*30)

		print("序号	姓名	性别	手机号码")
		i = 1
		for temp_info in stu_infos:
			print("%d	%s	%s	%s"%(i,temp_info['name'],temp_info['sex'],temp_info['phone']))
			i+=1
	elif key=='0':
		break
