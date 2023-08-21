#https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
import numpy as np
N,M = map(int,input().split())
arr = np.array([input().split() for i in range(N)], dtype='int')
print( np.max(np.min(arr,axis=1), axis=0) )