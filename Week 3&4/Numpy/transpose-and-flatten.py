#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
import numpy as np

N, M = input().split(' ')
N, M = int(N), int(M)
lst = []
for i in range(N):
    lst.append(input().split(' '))
arr = np.array(lst, dtype='int')
print(arr.T)
print(arr.flatten())