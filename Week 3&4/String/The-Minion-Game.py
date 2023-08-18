#Problem Link: https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

from collections import defaultdict

def minion_game(string):
    con, vow = 0, 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            vow += len(string) - i
        else:
            con += len(string) - i
        #print(string[i:j])
    if con > vow:
        print(f'Stuart {con}')
    elif con == vow:
        print('Draw')
    else:
        print(f'Kevin {vow}')
    
    
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)