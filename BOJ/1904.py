#BOJ - 01타일

'''
DP 기초
'''

import sys

input = sys.stdin.readline

n = int(input())
if n==1:
    print(1)
    sys.exit(0)
else:
    temp=[0 for _ in range(n)]
    temp[0], temp[1]=1, 2       
    for i in range(2,n):
        temp[i] = (temp[i-1]+temp[i-2])%15746
print(temp[n-1])
