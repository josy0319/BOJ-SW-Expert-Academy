#BOJ - N과 M(2)

'''
backtracking
&
combinations
'''

import sys

input = sys.stdin.readline

def solve(num, L):
    global res
    if num-1 == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
    else:
        for i in range(L, n+1):
            if ch[i]==0:
                ch[i]=1
                res[num-1]=i
                solve(num+1, i+1)
                ch[i]=0

n, m = map(int, input().split())
res = [0]*(m+1)
ch = [0]*(n+1)

solve(1, 1)
