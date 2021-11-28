Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import numpy as np
from numpy import *
from math import *
from matplotlib.pyplot import *
from sympy import *


def taylor(x):
    y = 0
    d1 = diff(f, x)
    d2 = diff(d1, x)
    d3 = diff(d2, x)
    d4 = diff(d3, x)
    print('d1=', d1, 'd2=', d2, 'd3=', d3, 'd4=', d4)
    y += f + d1 * x + d2 * (x - 0) ** 2 / 2 + d3 * (x - 0) ** 3 / 6 + d4 * (x - 0) ** 4 / 24
    print('y=', y)
    return y


x = symbols('x')
f = e ** (-x) + x ** 2
taylor_x = taylor(x)

plt  = plot(f, taylor_x, (x, -1, 1))
plt.title("Tymoshenko Volodymyr LB11")
plt.xlabel('х')
plt.ylabel('y')
plt.show()