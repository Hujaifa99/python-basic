# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for _ in range(N):
    try:
        a = input()
        a, b = int(a[0]), int(a[-1])
        print(f"{int(a//b)}")
    except Exception as e:
        print (f"Error Code: {e}")
