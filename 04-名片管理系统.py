#1.打印功能提示
print("="*50)
print("名片管理系统 V0.01")
print("1.添加一个新的名片")
print("2.删除一个名片")
print("3.修改一个名片")
print("4.查询一个名片")
print("5.显示所有名片")
print("6.退出系统")
print("="*50)
#创建一个空列表
card_infors = []
while True:

		#2.获取用户的输入
		num = int(input("请输入操作序号："))

		#3.根据用户的数据执行相应的功能
		if num==1:
			new_name = input("请输入新的名字：")
			new_qq = input("请输入新的QQ号：")
			new_wechat = input("请输入新的微信：")
			new_addr = input("请输入新的地址：")
			#定义一个新的字典，用来存储一个新的名片
			new_infor = {}
			new_infor['name'] = new_name
			new_infor['qq'] = new_qq
			new_infor['wechat'] = new_wechat
			new_infor['addr'] = new_addr
			
			card_infors.append(new_infor)
			print(card_infors)
		elif num==2:
			#删除
			search_flag = 0
			search_name = input("请输入要delete的姓名:")
			i = 0
			for temp in card_infors:
				if temp['name']==search_name:
					print("找到了,and delete")
					del card_infors[i]
					search_flag = 1
				i+=1
			if search_flag==0:
				print("查无此人")
			

		elif num==3:
			#change
			pass

		elif num==4:#查询
			search_flag = 0
			search_name = input("请输入要查询的姓名:")
			for temp in card_infors:
				if temp['name']==search_name:
					print("找到了")
					search_flag = 1

			if search_flag==0:
				print("查无此人")
		elif num==5:
			print("姓名\tQQ\t微信\t地址")
			for temp in card_infors:
				print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['wechat'],temp['addr']))
		elif num==6:
			break
		else:
			print("您的输入有误，请重新输入")
		print("\n")
