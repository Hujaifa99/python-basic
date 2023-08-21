#Problem Link: https://www.hackerrank.com/challenges/re-group-groups/problem
import re
s = input()
x = re.search(r'([a-zA-Z0-9])\1',s)
if x:
    print(x.group(1))
else: print(-1)