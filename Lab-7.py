import numpy as np
import pandas as pd
n = int(input('Enter the no. of variables: '))
A=[]
print("Enter the augmented matrix: ")
for i in range( n):
    row = list(map(float, input(f'Enter {i+1}th row: ').split()))
    A.append(row)
A = np.array(A)
print("The augmented matrix is: ")
print(np.matrix(A))
x = np.array(list(map(float, input(f'Enter initial vector : ').split())))
print("The initial guess is: \n", x)
e = float(input('Enter the error tolerance: '))
N = int(input('Enter the maximum number of iterations: '))
itr = 1
T = []
while itr<=N:
    x_old= np.copy(x)
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i][j] * x[j]
        x[i] = (A[i][-1] - s) / A[i][i]
    T.append([itr]+[x[i] for i in range(n)])
    err = abs(x - x_old)
    if np.all(err < e):
        break
    itr +=1
if itr>N:
    print("The solution  did not converge within the maximum number of iterations.")
else:
    T = pd.DataFrame(T, columns=['Iteration'] + [f'x{i+1}' for i in range(n)])
    print(T.to_string(index=False))
    print("The solution is :")
    for i in range(n):
        print(f"x{i+1} = {x[i]} at iteration {itr}")