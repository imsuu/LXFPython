from types import MethodType

class Student(object):
	"""docstring for Student"""
	__slots__ = ('name','age')
	
def set_age(self,age):
	self.age = age

s = Student()
s.name = 'Imsuu'
# print(s.name)
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print(s.age)		
s.age = 25
s.score = 99