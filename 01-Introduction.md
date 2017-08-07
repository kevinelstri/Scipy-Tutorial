SciPy是在Python的Numpy扩展基础上建立的数学算法和函数的集合。它为交互式Python会话增加了强大的功能，为用户提供了操作和可视化数据的高级命令和类。在SciPy中，交互式Python会话变成了数据处理和系统原型环境，与MATLAB、IDL、Octave、R-lab和SciLab等系统竞争。

将SciPy基于Python的好处是使得一种强大的编程语言可以用于开发复杂的程序和专门的应用程序。使用SciPy的科学应用得益于世界各地的开发人员在软件领域的众多领域中的模块的开发。从并行编程到web和基于的数据程序和类的所有东西都已被Python程序员所使用。除了在SciPy中的数学库之外，所有这些功能都是可用的。

本教程让第一次使用SciPy的用户了解一些最重要的特性。它假定用户已经安装了SciPy包。假设有一些通用的Python工具，例如可以通过使用Python发行版的教程来获得。为了进一步介绍，用户将被定向到Numpy文档。

~~~python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg, optimize
~~~

| subpackage  | description |
| ----------- | ----------- |
| cluster     | 聚类算法        |
| constants   | 物理和数学常量     |
| fftpack     | 快速傅里叶变换     |
| integrate   | 积分和常微分方程    |
| interpolate | 插值和平滑样条函数   |
| io          | 输入输出        |
| linage      | 线性代数        |
| ndimage     | n维图像处理      |
| odr         | 正交距离回归      |
| optimize    | 优化和求根方程     |
| signal      | 信号处理        |
| sparse      | 稀疏矩阵和相关程序   |
| spatial     | 空间数据结构和算法   |
| special     | 特殊函数        |
| stats       | 统计分布和函数     |

