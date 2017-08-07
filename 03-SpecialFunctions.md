# Special Functions

~~~python
from scipy import special
~~~

Functions: airy, elliptic, bessel, gamma, beta, hypergeometric, parabolic cylinder, mathieu, spheroidal wave, struve, and kelvin.

查看special中的方法，使用help(special)命令：

~~~python
>>> from scipy import special
>>> help(special)
Help on package scipy.special in scipy:
NAME
    scipy.special
FILE
    c:\python27\lib\site-packages\scipy\special\__init__.py
DESCRIPTION
    ========================================
    Special functions (:mod:`scipy.special`)
    ========================================
    ...
~~~

## Bessel Functions  贝塞尔函数

![2](C:\Users\kevinelstri\Desktop\2.png)

| 方法       | 描述               |
| -------- | ---------------- |
| jv       | 贝塞尔函数的实值序和复变函数   |
| jn       | 贝塞尔函数的别称         |
| jve      | 成倍扩展的贝塞尔函数       |
| yn       | 第二类贝塞尔函数（整数）     |
| yv       | 第二类贝塞尔函数（实数）     |
| yve      | 成倍扩展的第二类贝塞尔函数    |
| kn       | 修正第二类贝塞尔函数（整数阶）  |
| kv       | 修正第二类贝塞尔函数（实数阶）  |
| kve      | 指数比例修正贝塞尔函数的第二类  |
| iv       | 修正的贝塞尔函数         |
| ive      | 指数级修正的贝塞尔函数      |
| hankel1  | 第一类汉克尔函数         |
| hankel1e | 成倍缩放汉克尔函数的第一类    |
| hankel2  | 第二类汉克尔函数         |
| hankel2e | 成倍缩放Hankel函数的第二类 |



~~~python
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
print y
print z
~~~

~~~
Output:
[[ 0.          0.          0.         ...,  0.          0.          0.        ]
 [ 0.02040816  0.02024061  0.01974071 ...,  0.01974071  0.02024061
   0.02040816]
 [ 0.04081633  0.04048123  0.03948142 ...,  0.03948142  0.04048123
   0.04081633]
 ..., 
 [ 0.95918367  0.95130879  0.92781344 ...,  0.92781344  0.95130879
   0.95918367]
 [ 0.97959184  0.9715494   0.94755415 ...,  0.94755415  0.9715494
   0.97959184]
 [ 1.          0.99179001  0.96729486 ...,  0.96729486  0.99179001  1.        ]]

[[  0.00000000e+00   0.00000000e+00   0.00000000e+00 ...,  -0.00000000e+00
   -0.00000000e+00  -0.00000000e+00]
 [  0.00000000e+00   2.60973799e-03   5.17662416e-03 ...,  -5.17662416e-03
   -2.60973799e-03  -4.99855836e-18]
 [  0.00000000e+00   5.21947599e-03   1.03532483e-02 ...,  -1.03532483e-02
   -5.21947599e-03  -9.99711673e-18]
 ..., 
 [  0.00000000e+00   1.22657686e-01   2.43301336e-01 ...,  -2.43301336e-01
   -1.22657686e-01  -2.34932243e-16]
 [  0.00000000e+00   1.25267424e-01   2.48477960e-01 ...,  -2.48477960e-01
   -1.25267424e-01  -2.39930801e-16]
 [  0.00000000e+00   1.27877162e-01   2.53654584e-01 ...,  -2.53654584e-01
   -1.27877162e-01  -2.44929360e-16]]

[[ 0.          0.          0.         ...,  0.          0.          0.        ]
 [ 0.03428642  0.03400492  0.03316507 ...,  0.03316507  0.03400492
   0.03428642]
 [ 0.06841567  0.06785397  0.06617812 ...,  0.06617812  0.06785397
   0.06841567]
 ..., 
 [ 0.05622525  0.05576364  0.05438639 ...,  0.05438639  0.05576364
   0.05622525]
 [ 0.02789893  0.02766988  0.02698649 ...,  0.02698649  0.02766988
   0.02789893]
 [-0.         -0.         -0.         ..., -0.         -0.         -0.        ]]
~~~

~~~python
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
~~~

![3](C:\Users\kevinelstri\Desktop\3.png)

一般贝塞尔函数是下列常微分方程的标准解函数y(x):

![4](C:\Users\kevinelstri\Desktop\4.png)

这类函数的解无法使用初等函数来表示。

贝塞尔函数的具体形式随上述方程中任意实数α变化而变化（α被称为其对应贝塞尔函数的阶数），最常见的情形为α是整数n，对应解为n阶贝塞尔函数。