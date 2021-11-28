Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5])
y = np.array([0.91, 0.88, 0.85, 0.83, 0.83, 0.85, 0.9, 0.98, 0.84, 0.85])

x1 = sum(x)/10
x2 = sum(x**2)/10
y1 = sum(y)/10
yx = sum(x*y)/10

a1 = (yx - x1*y1)/(x2 - x1**2)
a0 = y1 - a1 * x1

x_graph = np.array([-6 , 6])
y_graph = np.array(a0 + a1*x_graph)


plt.plot(x_graph , y_graph)
plt.title("Tymoshenko Volodymyr LB12")
plt.xlabel('х')
plt.ylabel('y')
plt.grid()
plt.show()
