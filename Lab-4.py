import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input('Enter the equation with variable x using Python syntax: ')
def F(x, eqn):
    
    return eval(eqn)

def f(x):
    return F(x, eqn)

def df(x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

x0 = float(input("Enter the initial guess: "))
e = float(input('Enter the tolerable error: '))
N = int(input('Enter the maximum number of iterations: '))
itr = 1
A = []
m = []
while itr <= N:
    fx = f(x0)
    dfx = df(x0)
    if dfx == 0:
        print("Zero derivative. No solution found.")
        break
    x1 = x0 - fx / dfx
    m.append(x1)
    A.append([itr, x0, fx, dfx, x1])
    if abs(f(x1)) < e:
        A = pd.DataFrame(A, columns=['iteration', 'x0', 'f(x0)', "f'(x0)", 'x1'])
        print(A)
        print(f"\nThe approximate root is {x1} found in {itr} iterations.")
        break
    x0= x1
    itr += 1
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
plt.title('Newton Raphson  Method')
plt.scatter(m, f(m))
for i, val in enumerate(m):
    plt.text(val, f(val), f'{i + 1}')
plt.show()