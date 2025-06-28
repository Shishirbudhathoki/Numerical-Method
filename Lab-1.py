import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

equ = input('Enter the equation with variable x using python syntax: ')

def F(x, equ):
    
    return eval(equ)

def f(x):
    return F(x, equ)

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
        c = (a + b) / 2
        m.append(c)
        A.append([itr, a, b, c, f(a), f(b), f(c)])

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        error = abs(b - a)

        if error < e:
            A = pd.DataFrame(A, columns=['iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
            print(A)
            print(f"The approximate root is {(a + b) / 2} found in {itr} iterations.")
            break

        itr += 1

    if itr > N:
        print(f'Solution does not converge in {N} iterations')

    m = np.array(m)
    x = np.linspace(-5, 5, 1000)

    #plt.plot(x, [f(val) for val in x], color='red', label=equ, linestyle="--")
    plt.plot(x, f(x) , color='red', label=equ, linestyle="--")
    plt.axhline(0, color='black')
    plt.axvline(0, color='blue')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Bisection Method')
    plt.scatter(m, f(m))

    for i, val in enumerate(m):
        plt.text(val, f(val), f'{i + 1}')
    plt.show()
