#https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
import numpy as np
N, M = map(int,input().split())
arr = np.array([input().split() for i in range(N)], dtype='int')
print(np.prod(np.sum(arr,axis=0), axis=0) )