#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
import numpy as np
N,M = map(int,input().split())
arr = np.array([input().split() for i in range(N)], dtype='int')
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(round(np.std(arr,axis=None), 11))
