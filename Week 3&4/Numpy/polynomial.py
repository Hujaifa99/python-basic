#https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
import numpy as np
a = np.array(input().split(" "),float)
x = int(input())
print(np.polyval(a,x))