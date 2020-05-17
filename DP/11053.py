#BOJ - 가장 긴 증가하는 부분 수열

'''
DP 동적계획법
'''

import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

res = [1]*(n)
res[0]=1
for i in range(1,n):
    for j in range(i-1,-1,-1):
        if seq[j]<seq[i]:
            res[i]=max(res[i], res[j]+1)
print(max(res))
