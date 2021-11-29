from scipy.interpolate import UnivariateSpline
import mathplotlib.pyplot as plt
from numpy import *

x = [0.7, 0.8, 1.2, 1.5, 1.7]
y = [4.54, 6.14, 5.43, 3.72, 4.18]

spl = UnivariateSpline(x,y)
xs = linspace(0.7, 1.7, 1000)
plt.plot(x,y, 'ro', xs, spl(xs), 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('1')
plt.title('Tymoshenko Volodymyr FIT 2-4')
plt.show()
