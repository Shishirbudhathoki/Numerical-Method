# To solve initial value problem using Heun's method

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
    y_predictor=y+h*f(x,y)
    y_corrector=y+h/2*(f(x,y)+ f(x+h,y_predictor))
    x=x+h
    y = y_corrector
    T.append([x,y])
    x_list.append(x)
    y_list.append(y)


T = pd.DataFrame(T,columns=['x','y'])
print("Solution is : ")
print(T)

plt.plot(x_list , y_list ,marker='o' ,label="Solution by Heun's method")
plt.title("Solution by Heun's method")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

