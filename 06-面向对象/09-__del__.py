class Person(object):
	
	def __init__(self, name, age):
		#只要属性名前面有2个下划线，那么就表示 私有的属性
		#所谓的私有，不能在外部使用 对象名.属性名获取
		#原来没有添加__的属性， 默认就是 公有
		self.__name = name
		self.__age = age
	
	def __del__(self):
		print("-----del-----")

Mr_Wang = Person("老王",30)
del Mr_Wang
print("-----1-----")
