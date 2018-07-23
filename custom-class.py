# 定制类
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name:%s)' % self.name

	__repr__ = __str__

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

	def __call__(self):
		print('My name is %s' % self.name)

# print(Student('Michael'))
s = Student('Imsuu')
print(s())
print('-------------------')

class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0,1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b,self.a + self.b
		if self.a > 10000:
			raise StopIteration()
		return self.a

	def __getitem__(self,n):
		if isinstance(n, int):
			a,b =1, 1
			for x in range(n):
				a, b = b, a+b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a+b
			return L
		

for n in Fib():
	print(n)

f = Fib()
print(f[0])
print(f[10])

print(f[0:5])
print(f[:10])

class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path,path))

	def __str__(self):
		return self._path

	__repr__ = __str__

print(Chain().status.user.timeline.list)
