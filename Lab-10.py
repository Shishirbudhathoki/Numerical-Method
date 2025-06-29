# To find least eigen value and corresponding eigen vector of a square matrix by inverse power method.

import numpy as np
import pandas as pd
import scipy.linalg as slg

n = int(input('Enter the order of square matrix: '))
A=[]
for i in range( n):
    row = list(map(float, input(f'Enter {i+1}th row: ').split()))
    A.append(row)
A = np.array(A)
print('The square matrix is A : \n ',np.matrix(A))

def inv(A):
    try:
        return np.linalg.inv(A)
    except:
        print('Matrix is singular')
B= np.array(inv(A))


x = np.array(list(map(float, input(f'Enter output vector : ').split())))
x = np.array(x)
print('The initial vector is :\n',np.matrix(x))
e = float(input('Enter the tolerable error: '))
N = int(input('Enter the maximum number of iterations: '))
T =[]
itr =1
oldEv = 1
while itr<=N:
    Y=np.dot(B,x)
    maxEv =abs(max(Y,key=abs))
    x=Y/maxEv
    T.append([itr,maxEv]+[x[i] for i in range(n)])
    err= abs(maxEv-oldEv)
    if err<e:
        break
    oldEv = maxEv
    itr+=1
if itr>N:
    print(f'No Least eigenvalue found in {N} iterations')
else:
    T = pd.DataFrame(T, columns=['Iteration','Max eigenvalue'] + [f'x{i+1}' for i in range(n)])
    print(T.to_string(index=False))
    print(f'The Least eigenvalue is {1/maxEv} in {itr} iteration: ')
    print(f'The corresponding eigenvector is : \n',np.matrix(x))

