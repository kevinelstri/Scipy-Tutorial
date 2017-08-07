# coding:utf-8

import numpy as np

a = np.concatenate(([3], [0] * 5, np.arange(-1, 1.002, 2 / 9.0)))
print a

b = np.r_[3, [0] * 5, -1:1:9j]  # 行连接
print b

d = np.c_[[1, 2, 3], [4, 5, 6]]  # 列连接
print d
e = np.r_[[1, 2, 3], [4, 5, 6]]  # 行连接
print e

f = np.mgrid[0:5]  # 一维数组
print f
print

ff = np.mgrid[0:5, 0:5]  # N维
print ff

fff = np.mgrid[0:5:4j, 0:5:4j]  # N维
print fff

from numpy import poly1d

p = poly1d([3, 4, 5])
print p
print p * p  # 多项式平方
print p.integ()
print p.deriv()
print p(1)
print '-------------------------------------------'


def addsubtract(a, b):
    if a > b:
        return a - b
    else:
        return a + b


add = addsubtract(2, 3)
print add

vec_addsubtract = np.vectorize(addsubtract)
add = vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7])
print add

print '-------------------------------------------'
x = np.r_[-2:3]
print x
final = np.select([x > 3, x >= 0], [0, x + 2])
print final
print '-------------------------------------------'

from scipy import special


def drumhead_heght(n, k, distance, angle, t):
    kth_zero = special.jn_zeros(n, k)[-1]
    return np.cos(t) * np.cos(n * angle) * special.jn(n, distance * kth_zero)


theta = np.r_[0:2 * np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r * np.cos(theta) for r in radius])
y = np.array([r * np.sin(theta) for r in radius])
z = np.array([drumhead_heght(1, 1, r, theta, 0.5) for r in radius])
print x
print
print y
print
print z

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,z,rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
