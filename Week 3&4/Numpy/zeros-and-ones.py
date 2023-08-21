#https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true

import numpy as np
dimentions = list(map(int, input().split()))
print(np.zeros(dimentions, dtype='int'))
print(np.ones(dimentions, dtype='int'))