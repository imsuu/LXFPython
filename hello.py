#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(100 + 200 + 300)
print(0xff00)
print("I\'m \"OK\"!")
print(r"I\'m \"OK\"!")
print("a\nb\nc")
print('''d
e
f''')
print(3 < 2)
print(5 > 3 and 3 > 1)

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('Hello,%s' %'world')
print('%s have $%d.' %('Michael',1000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('growth rate: %d %%' % 7)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
s1 = 72
s2 = 85
r=(s2-s1)/s1*100
print('Hello, %s, 成绩提升了 %.1f%%' %('小明', r))

classmates = ['A','B','C']
print(classmates)
print(len(classmates))

print(classmates[1])
print(classmates[-1])

classmates.append('D')
print(classmates)
classmates.insert(1,'B0')
print(classmates)
classmates.pop()
classmates.pop(1)
print(classmates)

#tuple元组和list非常类似，但是tuple一旦初始化就不能修改
t = ('A','B','C')
t1 = (1)
t2 = (1,) 
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义

age = 3
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')

L = ['A','B','C','D','E','F','G']
print(L[:3])
print(L[1:4])
print(L[-2:])
#倒数第一个元素的索引是-1
print(L[-2:-1])
print(L[::2])