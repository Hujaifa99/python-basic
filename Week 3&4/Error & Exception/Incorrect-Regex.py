import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for _ in range(N):
    a = input()
    try:
        re.compile(a)
        print(True)
    except re.error as e:
        print(False)
