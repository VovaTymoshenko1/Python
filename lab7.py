import mathplotlib.pyplot as plt
from numpy import *

x = np.array([-2, 0, 2, 3], dtype = float)
y = np.array([-5, 7, 11, 25], dtype = float)

def langranz(x,y,t):
    z=0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i ==1:
                p1=p1*1; p2=p2*1
            else:
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z
xnew = np.linspace(np.sin(x), np.max(x), 100)
ynew = [langranz(x, y, i) for i in xnew]

plt.plot(x, y, 'o', xnew, ynew )
plt.xlabel('x')
plt.ylabel('y')
plt.legend('1')
plt.title('Tymoshenko Volodymyr FIT 2-4')
plt.show()
