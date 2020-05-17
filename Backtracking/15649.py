# N과 M(1)

'''
permutations
&
backtracking 
'''


# 1. permutation
import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
l = list(range(1, n+1))
pm = permutations(l, m)

for i in pm:
    for j in range(m):
        print(i[j], end=' ')
    print()
    
# 2. backtracking
import sys

input = sys.stdin.readline

def solve(L):
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                solve(L+1)
                ch[i]=0

n, m = map(int, input().split())
res = [0]*m
ch = [0]*(n+1)
print(ch)
solve(0)
