from functools import reduce
def f(x):
	return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def fn(x,y):
	return x*10+y

print(reduce(fn,[1,3,5,7,9]))