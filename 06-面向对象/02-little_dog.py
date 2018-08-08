class Dog:
	def __init__(self, color):
		self.color = color

	def bark(self):
		print("---旺旺叫---")
	
	def print_color(self):
		print("颜色为：%s"%self.color)

	def __str__(self):
		return "hahah"

def test(AAA):
	AAA.print_color()

John = Dog("白")
'''		
John.color = "白"
a = John.color
'''
liki = Dog("黑")
#John.print_color()	

#test(John)


print(John)
print(liki)
print(id(John))
print(id(liki))
