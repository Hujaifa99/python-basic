#https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
import numpy as np
N, M, P = input().split(' ')
N, M, P = int(N), int(M), int(P)
lst1 = []
for i in range(N):
    lst1.append(input().split(' '))
lst2 = []
for i in range(M):
    lst2.append(input().split(' '))
arr1, arr2 = np.array(lst1,dtype='int'), np.array(lst2,dtype='int')
print(np.concatenate((arr1,arr2), axis=0))


