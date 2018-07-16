from functools import reduce
def f(x):
	return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def fn(x,y):
	return x*10+y

print(reduce(fn,[1,3,5,7,9]))

def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty,['A',' ','',None,'B',' ','C'])))

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n >0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)
# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break

def is_palindrome(n):
    a=str(n)[::-1]
    return int(a)==n

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print( sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

def by_name(t):
	return t[0].lower()
def by_score(t):
	return t[1]
Lsorted = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(Lsorted,key=lambda x:x[0]))
print(sorted(Lsorted,key=lambda x:x[1]))
