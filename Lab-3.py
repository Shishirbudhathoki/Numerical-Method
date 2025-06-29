import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input('Enter the equation with variable x using Python syntax: ')

def F(x, eqn):
    
    return eval(eqn)

def f(x):
    return F(x, eqn)


a = float(input("Enter the first approximation: "))
b = float(input("Enter the second approximation: "))
e = float(input('Enter the tolerable error: '))
N = int(input('Enter the maximum number of iterations: '))

itr = 1
A = []
m = []

while itr <= N:
    fa = f(a)
    fb = f(b)
    if (fb - fa == 0):
        print("Denominator zero. Secant method fails.")
        break
    c = (a * fb - b * fa) / (fb - fa)
    fc = f(c)
    m.append(c)
    A.append([itr, a, b, c, fa, fb, fc])
    if abs(fc) < e:
        A = pd.DataFrame(A, columns=['iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
        print(A)
        print(f"\nThe approximate root is {c} found in {itr} iterations.")
        break
    a,b=b,c
    itr +=1
else:
    print(f"\nSolution does not converge in {N} iterations.")
m = np.array(m)
x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x), color='red', label=eqn, linestyle="--")
plt.axhline(0, color='black')
plt.axvline(0, color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Secant Method')
plt.scatter(m, f(m))
for i, val in enumerate(m):
    plt.text(val, f(val), f'{i + 1}')
plt.show()