#0.提示并获取要复制的文件名
name = input("请输入要复制的文件名:")


#1.打开要复制的文件
f_read = open(name,"r")

#2.创建一个新的文件，用来存储源文件的数据内容
find_position = name.rfind(".")
new_name = name[:find_position]+"[复件]"+name[find_position:]
f_write = open(new_name,"w")

#3.复制
#第一种方式
#content = f_read.read()
#f_write.write(content)

#第二种方式
#for line_content in f_read.readlines(): 
#	f_write.write(line_content)

#第三种方式
while True:
	line_content = f_read.readline()
	if len(line_content)>0:
		f_write.write(line_content)
	else:
		break

#4.关闭文件

f_read.close()
f_write.close()
