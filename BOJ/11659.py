#BOJ - 구간 합 구하기4

'''
DP(동적계획법) 기초
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
q = [list(map(int, input().split())) for _ in range(m)]

res=[0 for _ in range(n)]

for i in range(n):
    if i==0:
        res[i] = seq[i]
    else:
        res[i] = res[i-1]+seq[i]
for j in q:
    x, y = j[0], j[1]
    if x==1:
        print(res[y-1])
    else:
        print(res[y-1]-res[x-2])
