import numpy as np
import mathplotlib.pylab as plt

def ff(x):
    return 8*np.sin(x)*np.sin(2*x)/(x**(1/2))

x = np.arange(1,10,1)

plt.title("Lab7")
plt.xlabel('x')
plt.ylabal('y')

plt.plot(x, ff(x))
plt.grid()
plt.show()