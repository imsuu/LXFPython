import types
def fn():
	pass

print(type(fn)==types.FunctionType)
print(type((x for x in range(10)))==types.GeneratorType)

class Animal(object):
	"""docstring for Animal"""
	pass

class Dog(Animal):
	"""docstring for Dog"""
	pass

class Husky(object):
	"""docstring for Husky"""
	pass
		
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))

print(isinstance([1, 2, 3], (list, tuple)))

print(dir('ABC'))
print('ABC'.__len__())

class Student(object):
	"""docstring for Student"""
	name = 'Student'


s = Student()
print(s.name)
print(Student.name)

s.name = 'Imsuu'
print(s.name)
print(Student.name)

class Cname(object):
	"""docstring for Cname"""
	count = 0
	def __init__(self, name):
		Cname.count +=1
		self.name = name
if Cname.count !=0:
	print('测试失败')
else:
	bart = Cname('Bart')
	if Cname.count != 1:
		print('测试失败')
	else:
		lisa = Cname('Lisa')
		if Cname.count !=2:
			print('测试失败')
		else:
			print('Students:',Cname.count)