import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


equ = input('Enter the equation with variable x using Python syntax : ')

def f(x):
    return eval(equ)

a = float(input("Enter the first approximation: "))
b = float(input("Enter the second approximation: "))

if f(a) * f(b) > 0:
    print(f'No root lies in the interval ({a}, {b})')
else:
    e = float(input('Enter the tolerable error: '))
    N = int(input('Enter the maximum number of iterations: '))

    itr = 1
    A = []
    m = []

    while itr <= N:
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        m.append(c)
        A.append([itr, a, b, c, fa, fb, fc])

        if fa * fc < 0:
            b = c
        else:
            a = c

        if abs(fc) < e:
            A = pd.DataFrame(A, columns=['iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
            print(A)
            print(f"\nThe approximate root is {c} found in {itr} iterations.")
            break

        itr += 1

    else:
        print(f"\nSolution does not converge in {N} iterations.")


    m = np.array(m)
    x = np.linspace(-5, 5, 1000)
    
    plt.plot(x, f(x), color='red', label=equ, linestyle="--")
    plt.axhline(0, color='black')
    plt.axvline(0, color='blue')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Regukar Falsi Method')
    plt.scatter(m, f(m))
    
    for i, val in enumerate(m):
        plt.text(val, f(val), f'{i + 1}')
    plt.show()


    