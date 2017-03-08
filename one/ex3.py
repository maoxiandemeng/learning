# -*- coding: utf-8 -*-

L = ['Adam', 'Lisa', 'Bart', 'Paul']
# L[0:3]从索引0开始取，直到索引3为止，但不包括索引3 也可以这样表示L[:3]
# L[:] 从都到尾取出来
# L[0::3]从都到尾取出来每隔2位去一个数
print L[0:3]

L = range(1, 101)
# 取前10个数
print L[:10]
# 取3的倍数
print L[2::3]
# 取不大于50的5的倍数
print L[4:50:5]
# 取最后10个数
print L[-10:]
# 取最后10个5的倍数
print L[4::5][-10:]


def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
print d.values()
for v in d.values():
    print v


def toUppers(l):
    return [x.upper() for x in l if isinstance(x, str)]
print toUppers(['Hello', 'world', 101])

l = range(0, 9)
print [str(x)+str(y)+str(z) for x in l for y in l for z in l if x == z]

