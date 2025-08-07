# To evaluate the fx integrate limit(a,b) using simpson's 1/3 rule.
import numpy as np
import matplotlib.pyplot as plt  

a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the no. of partitions: "))
if n % 2 != 0:
    print('No. of partitions must be even')
    exit()
else:
    h = (b - a) / n
    func = input("Enter the integrant function in x using python syntax: ")

    def f(x, func):
        return eval(func)

    def y(x):
        return f(x, func)

    x = np.linspace(a, b, n + 1)
    ypoints = [y(xi) for xi in x]

    S1 = 0
    S2 = 0
    for i in range(1, n):
        if i % 2 != 0:
            S1 += ypoints[i]
        else:
            S2 += ypoints[i]

    I = (h / 3) * (ypoints[0] + 4 * S1 + 2 * S2 + ypoints[n])
    print(f"The approximation integral by Simpson's 1/3 rule is {I}")

    # Plotting
    plt.plot(x, ypoints, color='r', label='Best fit curve')
    xval = np.linspace(a - 10, b + 10, 1000)
    plt.plot(xval, [y(val) for val in xval], label='Eqn in curve')

    for i in range(0, n, 2):
        xs = x[i:i+3]
        ys = ypoints[i:i+3]
        plt.fill_between(xs, ys, color='lightblue', alpha=0.3)

    plt.title("Simpson's 1/3 Rule Approximation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()