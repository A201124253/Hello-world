class Person(object):
	
	def __init__(self, name, age):
		#只要属性名前面有2个下划线，那么就表示 私有的属性
		#所谓的私有，不能在外部使用 对象名.属性名获取
		#原来没有添加__的属性， 默认就是 公有
		self.__name = name
		self.__age = age

	def set_new_age(self, new_age):
		if new_age>0 and new_age<=100:
			self.__age = new_age
			
	def get_age(self):
		return self.__age
	
	def __test1(self):
		print("-----test1不会被对象.__test单独调用-----")
	
	def test2(self):
		self.__test1()
		print("-----test2可以调")

Mr_Wang = Person("老王",30)
age = Mr_Wang.get_age()
print("老王现在的年龄是%d"%age)
Mr_Wang.set_new_age(31)
age = Mr_Wang.get_age()
print(age)
Mr_Wang.test2()
