# Numpy交互

Scipy是在Numpy基础上建立的，对于一些基本的数组处理需要使用Numpy功能来处理：

~~~python
import numpy as np
np.some_function()
~~~

除了对一些功能进行更详细的描述，本教程还会讨论一些有用的命令。

~~~python
from scipy import some_module
some_module.some_function()
~~~

有一些类实例可以使用切片功能，可以为数组提供有效的功能。这部分将讨论一些功能(np.mgrid, np.ogrid, np.r\_, np.c\_)，便于快速构建数组：

~~~python
# codinng:utf-8
import numpy as np
a = np.concatenate(([3], [0] * 5, np.arange(-1, 1.002, 2 / 9.0)))  # 多列索引，多行索引
b = np.r_[3, [0] * 5, -1:1:10j]  # 10j表示范围内有10个数字
~~~

~~~python
Output:
        [ 3.          0.          0.          0.          0.          0.         -1.
         -0.77777778 -0.55555556 -0.33333333 -0.11111111  0.11111111  0.33333333
          0.55555556  0.77777778  1.        ]
        [ 3.          0.          0.          0.          0.          0.         -1.
         -0.77777778 -0.55555556 -0.33333333 -0.11111111  0.11111111  0.33333333
          0.55555556  0.77777778  1.        ]
~~~

注意：使用复数10j作为分段语法时，这种非标准的使用并不是步长，而是在这个范围内，产生点的数量，包括范围两端的数字。

~~~python
b = np.r_[3, [0] * 5, -1:1:9j]  # 范围内有9个数字
Output:	[ 3.    0.    0.    0.    0.    0.   -1.   -0.75 -0.5  -0.25  0.    0.25
  		  0.5   0.75  1.  ]
~~~

“r\_”表示行连接，“c\_”表示列连接

~~~python
d = np.c_[[1, 2, 3], [4, 5, 6]]  # 列连接
e = np.r_[[1, 2, 3], [4, 5, 6]]  # 行连接
Output d:[[1 4]
 		  [2 5]
 		  [3 6]]
Output e:[1 2 3 4 5 6]
~~~

mgrid函数用于切片，可以用来替换range函数：

~~~python
f = np.mgrid[0:5]  # 一维数组
ff = np.mgrid[0:5, 0:5]  # N维
fff = fff = np.mgrid[0:5:4j, 0:5:4j]  # N维
~~~

~~~python
Output:
	 f: [0 1 2 3 4]
	ff: [[[0 0 0 0 0]
          [1 1 1 1 1]
          [2 2 2 2 2]
          [3 3 3 3 3]
          [4 4 4 4 4]]

         [[0 1 2 3 4]
          [0 1 2 3 4]
          [0 1 2 3 4]
          [0 1 2 3 4]
          [0 1 2 3 4]]]
   fff: [[[ 0.          0.          0.          0.        ]
          [ 1.66666667  1.66666667  1.66666667  1.66666667]
          [ 3.33333333  3.33333333  3.33333333  3.33333333]
          [ 5.          5.          5.          5.        ]]

         [[ 0.          1.66666667  3.33333333  5.        ]
          [ 0.          1.66666667  3.33333333  5.        ]
          [ 0.          1.66666667  3.33333333  5.        ]
          [ 0.          1.66666667  3.33333333  5.        ]]]
~~~

# Polynomials多项式

在scipy中有两种方式来处理一维多项式，第一个是Numpy提供的poly1d类，这个类接受参数作为多项式的系数，可以用代数表达式、积分、微分和求值来对多项式对象进行操作，像一个多项式一样打印:

~~~python
from numpy import poly1d

p = poly1d([3, 4, 5])
print p  # 多项式
print p*p  # 多项式平方
print p.integ()
print p.deriv()
print p(1)
~~~

~~~python
Output:
         2
      3 x + 4 x + 5
         4      3      2
      9 x + 24 x + 46 x + 40 x + 25
         3     2
      1 x + 2 x + 5 x

      6 x + 4
      12
~~~

另一种处理多项式的方法是用数组的第一个元素作为系数的数组给出最高的系数。有一些显式的函数可以加、减、乘、除、积分、微分和求多项式的系数序列。

# vectorize功能

NumPy提供的特性之一是一个类vectorize，用于转换普通的Python函数，该函数接受标量，并将标量转换为“vectoriz函数”，与其他NumPy函数(即通用函数或函数)相同的广播规则。例如，假设有一个名为add减法的Python函数定义为:

~~~python
def addsubtract(a, b):
    if a > b:
        return a - b
    else:
        return a + b
add = addsubtract(2, 3)
~~~

它定义了两个标量变量的函数，并返回一个标量结果，类vectorize可以用来对这个函数进行“矢量化”，返回一个数组结果：

~~~python
vec_addsubtract = np.vectorize(addsubtract)
add = vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7])
print add
Output:[1 6 1 2]
~~~

# 类型处理

区别：np.iscomplex/np.isreal   和   np.iscomplexobj/np.isrealobj

前一对命令是基于数组的，并返回1和0的字节数组，提供了元素-智慧测试的结果。后一对命令是基于对象的，并返回一个描述整个对象测试结果的标量。

通常需要得到复数的实数和虚部。虽然复杂的数字和数组有返回这些值的属性，但是如果不确定对象是否会被完全赋值，那么最好使用函数形式np.real 和 np.image。这些函数成功地实现了任何可以转化为Numpy数组的功能。考虑函数np.real_if_close，它将一个复杂的数值与极小的虚数转换为实数。

有时需要检查一个数字是否为标量(int、long、float、complex、rank-0 array)。此功能提供一个函数共功能np.isscalar，它返回1或0。

# 其他函数

~~~python
x = np.r_[-2:3]
print x
y = np.select([x > 3, x >= 0], [0, x + 2])
print y
~~~

