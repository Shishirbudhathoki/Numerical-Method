# To solve initial value problem of first order by the R-K-4 method

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ode = input("Enter dy/dx in term of x and y using python syntax : ")
def F(x,y,ode):
    return eval(ode)
def f(x,y):
    return F(x,y,ode)

T=[]
x_list = []
y_list = []

x = float(input("Enter initial value of x : "))
y = float(input("Enter initial value of y : "))
h = float(input("Enter step size  : "))
n = int(input("Enter the number of steps : "))

T.append([x, y])
x_list.append(x)
y_list.append(y)

for i in range(n):
    k1=h*f(x,y)
    k2=h*f(x+h/2, y+k1/2)
    k3=h*f(x+h/2, y+k2/2)
    k4=h*f(x+h, y+k3)
    y=y+(1/6)*(k1+2*k2+2*k3+k4)
    x=x+h
    T.append([x,y])
    x_list.append(x)
    y_list.append(y)


T = pd.DataFrame(T,columns=['x','y'])
print("Solution is : ")
print(T)

plt.plot(x_list , y_list ,marker='o' ,label='Solution by R-K-4 method')
plt.title("Solution by R-K-4 method")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

