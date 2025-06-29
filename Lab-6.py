import numpy as np

n = int(input('Enter the no. of variables: '))
A=[]
print("Enter the augmented matrix: ")
for i in range( n):
    row = list(map(float, input(f'Enter {i+1}th row: ').split()))
    A.append(row)
A = np.array(A)
print("The augmented matrix is: ")
print(A)
for i in range(n):
    p_row = np.argmax(np.abs(A[i:, i]))+i
    A[[i, p_row]] = A[[p_row, i]]
    A[i] = A[i] / A[i,i] 
    for j in range(n):
        if j != i:
            A[j] = A[j] - A[j,i]* A[i]

print("The normal matrix is: ")
print(np.matrix(A))

x=A[:,-1]  
print("\n",x)
