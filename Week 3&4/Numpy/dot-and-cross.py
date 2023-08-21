#https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
import numpy as np
N = int(input())
arr1 = np.array([input().split() for i in range(N)], dtype='int')
arr2 = np.array([input().split() for i in range(N)], dtype='int')
print(np.dot(arr1,arr2))