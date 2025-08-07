# To evaluate integral f(x) of limit a to b using trapezoidal rule.

import numpy as np
import matplotlib.pyplot  as plt

a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the no. of integration: "))
h=(b-a)/n
func=input("Enter the integral function in x using python syntax: ")

def f(x, func):
    return eval(func)
def y(x):
    return f(x, func)

x=np.linspace(a,b,n+1)
I = 0
S = 0
for i in range(1,n):
    S+=y(x[i])
I=(h/2)*(y(x[0])+2*S+y(x[n]))
print(f"The approximate integral by trapezoidal rule is {I}.")

ypoints=[y(xi) for xi in x]
plt.plot(x,ypoints,color='r',label='Best fit curve')
xval=np.linspace(a-10,b+10,1000)
plt.plot(xval,[y(xi) for xi in xval], label='Eqn in curve')
for i in range(n):
    xs=[x[i],x[i],x[i+1],x[i+1]]
    ys=[0,ypoints[i],ypoints[i+1],0]
    plt.fill(xs,ys,color='pink',edgecolor='blue',alpha=0.2)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Trapezoidal Rule')
plt.grid(True)
plt.show()
