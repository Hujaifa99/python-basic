#https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
import numpy as np
n = input()
n = n.split(' ')
arr = np.array(n,dtype='int')
arr = np.reshape(arr,(3,3))
print(arr)