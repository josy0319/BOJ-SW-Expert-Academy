#BOJ - 동전0

'''
그리디 알고리즘
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
res = 0
start = len(c)-1
while True:
    for i in range(start, -1, -1):
        if k-c[i]>=0:
            res+=1
            k-=c[i]
            start=i
            break
    if k==0:
        break
print(res)
