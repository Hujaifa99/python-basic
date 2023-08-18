#Problem Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = input()
exp = '[+-.]?[0-9]*\.[0-9]+'
for i in range(int(N)):
    print( bool(re.fullmatch(exp, input() )) )