import numpy as np

n = int(input('Enter the no. of variables: '))
A=[]
print("Enter the augmented matrix: ")
for i in range( n):
    row = list(map(float, input(f'Enter {i+1}th row: ').split()))
    A.append(row)
A = np.array(A)
print("The augmented matrix is: ")
print(np.matrix(A))
for i in range(n):
    p_row = np.argmax(np.abs(A[i:, i]))+i
    A[[i, p_row]] = A[[p_row, i]]  
    for j in range(i+1, n):
        A[j] = A[j] - A[j][i] / A[i][i] * A[i]
        A = np.round(A).astype(int)

print("The upper triangular matrix  is: ")
print(np.matrix(A))
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (A[i][-1] - np.sum(A[i][i+1:n]* x[i+1:n])) / A[i,i]
print("The solution is: ")

for i in range(n):
    print(f"x{i+1} = {round(x[i])}")