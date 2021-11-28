import numpy as np
import math

mas_x=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
mas_y=[10.517, 10.193, 9.807, 9.387, 8.977, 8.637, 8.442, 8.482, 8.862, 9.701, 11.132, 13.302]
h = mas_x[1] - mas_x[0]

def fun(mas_y,r):
    mas=[]
    for i in range(len(mas_y)):
        mas.append(mas_y[i] - mas_y[i-1])
    mas.pop(0)
    if r == 1:
        return mas
    else:
        r -=1
        return fun(mas, r)
yx1=1/h*((fun(mas_y, 1)[1]) - (fun(mas_y, 2)[1])/2 + (fun(mas_y, 3)[1])/3 - (fun(mas_y, 4)[1])/4 )
yx2=1/h**2*((fun(mas_y, 2)[1])-(fun(mas_y, 3)[1])+11/12*(fun(mas_y, 4)[1]))

print(fun(mas_y, 3))
print (yx1)
print (yx2)