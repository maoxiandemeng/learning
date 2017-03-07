# -*- coding: utf-8 -*-

# t = ('aaa', 'bbb', 'ccc')
t = ('aaa', 'bbb', 'ccc', ['AAA', 'BBB'])
l = t[3]
# print t

age = 20
# if age >= 18:
#     print 'age大于18'
# else:
#     print 'age小于18'

# if age >= 22:
#     print 'age大于22'
# elif age >= 20:
#     print 'age大于20'
# else:
#     print 'age小于18'

# L = [75, 92, 59, 68]
# sum = 0.0
# for i in L:
#     sum+=i
# print sum / 4

# sum2 = 0
# x = 1
# while x <= 100:
#     if x % 2 != 0:
#         sum2 += x
#     x += 1
# print sum2

# sum3 = 0
# x = 1
# n = 1
# while True:
#     sum3 += x
#     x *= 2
#     print x
#     if n >= 20:
#         break
#     n += 1
# print sum3

# sum4 = 0
# x4 = 0
# while True:
#     x4 += 1
#     if x4 > 100:
#         break
#     else:
#         if x4 % 2 == 0:
#             continue
#         print x4
#     sum4 += x4
# print sum4

# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     for y in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#         if x < y:
#             print str(x) + '<' + str(y)


d = {
    'aaa': 95,
    'bbb': 85,
    'ccc': 59
}
# 添加
# d.setdefault('ddd', 65)
# 删除
# d.pop('aaa', 95)
# d['aaa']  d.get('aaa')获得对应aaa的值
# print d
# print len(d)

s = set(['A', 'B', 'C', 'D'])
l = ['A', 'C', 'E', 'F']
for name in l:
    if name in s:
        continue
    s.add(name)
print s
