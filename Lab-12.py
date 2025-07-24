import numpy as np
import scipy.linalg as slg
import matplotlib.pyplot as plt

print('To find the curve y = a + bx + cx^2')

n = int(input("No. of data points : "))
X = np.array(list(map(float, input("Enter all x-data: ").split())))
Y = np.array(list(map(float, input("Enter all y-data: ").split())))

X_input = X.copy()

A = [
    [n, np.sum(X), np.sum(X**2)],
    [np.sum(X), np.sum(X**2), np.sum(X**3)],
    [np.sum(X**2), np.sum(X**3), np.sum(X**4)]
]

B = [np.sum(Y), np.sum(X * Y), np.sum(X**2 * Y)]

print("The coefficient matrix A:\n", np.matrix(A))
print("The output matrix B:\n", np.matrix(B))

coeff = slg.solve(A, B)
print(f'Curve of best fit: y = {coeff[0]:.4f} + {coeff[1]:.4f}*x + {coeff[2]:.4f}*x^2')

X = np.linspace(min(X_input) - 2, max(X_input) + 2, 100)
Y_fit = coeff[0] + coeff[1]*X + coeff[2]*X**2

plt.plot(X, Y_fit, label='Best fit curve', color='blue')
plt.scatter(X_input, Y, color='red', label='Data points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Curve Fitting')
plt.legend()
plt.grid()
plt.show()

