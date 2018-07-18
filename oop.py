class Student(object):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name,self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(lisa.get_name(),lisa.get_grade())

class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	"""docstring for Dog"""
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	"""docstring for Cat"""
	pass
		
dog = Dog()
dog.run()

cat = Cat()
cat.run()