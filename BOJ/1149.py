#BOJ - RGB거리

'''
DP 동적계획법
'''

import sys

input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*3 for _ in range(n)]
temp[0] = rgb[0]
for i in range(1,n):
    for j in range(3):
        if j==0:
            x, y=1, 2
        elif j==1:
            x, y=0, 2
        else:
            x, y=0, 1
        temp[i][j]=min(temp[i-1][x], temp[i-1][y])+rgb[i][j]
print(min(temp[-1]))
    
