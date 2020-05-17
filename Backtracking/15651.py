#BOJ - N과 M(3)

'''
backtracking

'''
import sys

input = sys.stdin.readline

def solve(L):
    if L==m+1:
        for i in range(1,m+1):
            print(res[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            res[L] = i
            solve(L+1)

n, m = map(int, input().split())
res = [0]*(m+1)
solve(1)
