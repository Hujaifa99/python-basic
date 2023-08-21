#https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
import numpy

def arrays(arr):
    arr = numpy.array(arr, dtype='float')
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)