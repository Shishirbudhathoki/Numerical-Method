# To solve the system of linear equation by LU Decomposition method 
import numpy as np
import scipy.linalg as slg

n = int(input('Enter the no. of variables: '))
A=[]
for i in range( n):
    row = list(map(float, input(f'Enter {i+1}th row: ').split()))
    A.append(row)
A = np.array(A)
print('The coef. matrix is A : \n ',np.matrix(A))
B = np.array(list(map(float, input(f'Enter output vector : ').split())))
B = np.array(B)
print('The output matrix in B:\n',np.matrix(B))
P,L,U = slg.lu(A)
lum = slg.lu_factor(A)
print('The lower triangular matrix is L:\n ',L)
print('The upper triangular matrix is U:\n ',U)
print('The permutation triangular matrix is P:\n ',P)
x=slg.lu_solve(lum,B)
print('The solution is :')
for i in range (n):
    print(f'x{i+1}={x[i]}')