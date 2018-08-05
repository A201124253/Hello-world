#0.提示并获取要复制的文件名
name = input("请输入要复制的文件名")


#1.打开要复制的文件
f_read = open(name,"r")

#2.创建一个新的文件，用来存储源文件的数据内容
new_name = 
f_write = open("test[复件].txt","w")

#3.复制
content = f_read.read()
f_write.write(content)

#4.关闭文件

f_read.close()
f_write.close()
