#https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
import numpy as np
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
lst1=[]
for i in range(N):
    lst1.append(list(map(int,input().split())))
lst2=[]
for i in range(N):
    lst2.append(list(map(int,input().split())))
lst1, lst2 = np.array(lst1), np.array(lst2)
print(lst1+lst2)
print(lst1-lst2)
print(lst1*lst2)
print(np.floor_divide(lst1,lst2))
print(lst1%lst2)
print(lst1**lst2)    


