# To find dominant eigen value and corresponding eigen vector of a square matrix of power method.

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
x = np.array(list(map(float, input(f'Enter initial vector : ').split())))
x = np.array(x)
print('The initial vector is :\n',np.matrix(x))
e = float(input('Enter the tolerable error: '))
N = int(input('Enter the maximum number of iterations: '))
T =[]
itr =1
oldEv =1 
while itr<=N:
    Y=np.dot(A,x)
    maxEv =abs(max(Y,key=abs))
    x=Y/maxEv
    T.append([itr,maxEv]+[x[i] for i in range(n)])
    err= abs(maxEv-oldEv)
    if err<e:
        break
    oldEv = maxEv
    itr+=1
if itr>N:
    print(f'No dominant eigenvalue found in {N} iterations')
else:
    T = pd.DataFrame(T, columns=['Iteration','Max eigenvalue'] + [f'x{i+1}' for i in range(n)])
    print(T.to_string(index=False))
    print(f'The dominant eigenvalue is {maxEv} in {itr} iteration: ')
    print(f'The corresponding eigenvector is : \n',np.matrix(x))




    #  2 1 0
    #  1 2 0
    #  0 0 -1

    # 0 1 0
    # 1e-10

    # ans: 3 --->1 1 0