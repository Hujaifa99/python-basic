#Problem Link: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    # your code goes here
    for i in range(int(len(string) / k)):
        s = string[i*k:(i+1)*k]
        s = list(s)
        seen = []
        for i in s:
            if i not in seen:
                seen.append(i)
        print(''.join(seen))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)