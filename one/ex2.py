# array = [1, 2, 5, 3, 6, 8, 4]
# for i in range(len(array) - 1, 0, -1):
#     print i
#     for j in range(0, i):
#         print j
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
# print array

# L = [x*x for x in range(1, 101)]
# print sum(L)
# s = 0
# for x in range(1, 101):
#     s += x*x
#     print x
# print s


# def square_of_sum(l):
#     s = 0
#     for x in l:
#         s += x*x
#     return s
#
# print square_of_sum([1, 2, 3, 4, 5])
# print square_of_sum([-5, 0, 5, 15, 25])
# import math
#
#
# def move(x, y, step, angle):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x1, y1 = move(100, 100, 60, math.pi / 6)
# print x1, y1

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# print fact(100)

# def move(n, a, b, c):
#     if n == 1:
#         print a+'-->'+c
#         return
#     move(n-1, a, c, b)
#     print a+'-->'+c
#     move(n-1, b, a, c)
#
# move(2, 'A', 'B', 'C')


# def power(x, n):
#     s = 1
#     while n > 0:
#         n -= 1
#         s = s * x
#     return s
# print power(3, 2)

# def average(*args):
#     if args:
#         return 1.0*sum(args)/len(args)
#     else:
#         return 0.0
#
# print average()
# print average(1, 2)
# print average(1, 2, 2, 3, 4)




