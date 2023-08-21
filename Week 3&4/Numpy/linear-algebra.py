#https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
import numpy as np
n = int(input())
a = np.array([input().split(" ") for i in range(n)],float)
print(round(np.linalg.det(a),2))