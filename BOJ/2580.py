#BOJ - 스도쿠

'''
backtracking 응용
검출코드 모듈화
'''

import sys
input = sys.stdin.readline

def solve(L):
    if L==len(zero_list):
        for i in s:
            for j in range(9):
                print(i[j], end=' ')
            print()
        sys.exit(0)
    else:
        for i in range(1, 10):
            x, y = zero_list[L][0], zero_list[L][1]
            if condition(x, y, i):
                s[x][y]=i
                solve(L+1)
                s[x][y]=0

def condition(x, y, k):
    if k in s[x]:
        return False
    for i in range(9):
        if s[i][y]==k:
            return False
    if x%3==1:
        x-=1
    elif x%3==2:
        x-=2
    if y%3==1:
        y-=1
    elif y%3==2:
        y-=2
    for i in range(x, x+3):
        for j in range(y, y+3):
            if s[i][j]==k:
                return False     
    return True

s = [list(map(int, input().split())) for _ in range(9)]

zero_list = []
for i in range(9):
    for j in range(9):
        if s[i][j]==0:
            zero_list.append((i,j))
solve(0)

