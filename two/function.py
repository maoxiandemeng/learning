# -*- coding: utf-8 -*-


def func(g, arr):
    return [g(x) for x in arr]
# func 是一个高阶函数，它接收两个参数，第 1 个参数是函数，第 2 个参数是数组，
# func 的功能是将函数 g 逐个作用于数组 arr 上，并返回一个新的数组


def f1(x):
    return x+1

print func(f1, [1, 2, 3, 4])

print map(f1, [1, 4, 6, 8])
print list(map(f1, [1, 4, 6, 8]))
# list 转换，是为了兼容 Python3，在 Python2 中 map 直接返回列表，Python3 中返回迭代器。


print reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1*2*3*4
print reduce(lambda x, y: x * y, [1, 2, 3, 4], 5)  # 5*1*2*3*4


print list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print filter(lambda x: x > 'g', 'gameOver')

f = lambda x: x * 2
print (lambda x: x * 2)(4)
print f(4)




