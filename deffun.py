import functools

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,3,5,7,9)
print(f)

print(f())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

def count2():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs

f4,f5,f6 = count2()
print(f4())
print(f5())
print(f6())

def build(x,y):
	return lambda: x*x+y*y
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1000000',base=10))

max2 = functools.partial(max, 10)
print(max2(5,7,8))