# To find Lagrange interpolation for the given data.

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

n = int(input("No. of data points : "))
X = np.array(list(map(float,input("Enter all x-data: ").split())))
Y = np.array(list(map(float,input("Enter all y-data: ").split())))
xp = float(input("Enter the point to interpolate: "))
S=0
x= sp.symbols('x')
for i in range (n):
    lf=1
    for j in range(n):
        if j!=i:
            lf *=(x-X[j])/(X[i]-X[j])
    S+=Y[i]*lf

poly = sp.simplify(S)

print("Lagrange interpolation polynomial in : \n ",poly)
int_val = poly.subs(x,xp)
print(f"The interpolated value at x ={xp} is {round(int_val,3)}.")

f=sp.lambdify(x,poly,'numpy')
x_val = np.linspace(min(X)-2,max(X)+2 ,1000)


plt.plot(x_val, f(x_val), color='red', linestyle="--",label='Lagrange Interpolation')
plt.axhline(0, color='black')
plt.axvline(0, color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f')
plt.legend()
plt.title('Lagrange Interpolation')
plt.scatter(X ,Y)
for i, val in enumerate(X):
    plt.text(val, Y[i], f'{i + 1}')
plt.show()
