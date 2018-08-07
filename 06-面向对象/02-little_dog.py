class Dog:
	def __init__(self, color):
		self.color = color



	def bark(self):
		print("---旺旺叫---")
	
	def print_info(self):
		print(self.color)

John = Dog("白")
'''		
John.color = "白"
a = John.color
'''
John.print_info()	
