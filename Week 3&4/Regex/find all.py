#Problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
s = input()
import re
x = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU][aeiouAEIOU]+(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])', s)
if x:
    for i in range(len(x)):
        print(x[i])
else: print(-1)
