#BOJ - 정수 삼각형

'''
DP 동적계획법
'''

import sys

input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split()))+[0] for _ in range(n)]
temp = [[0]*n for i in range(n)]
temp[0][0] = tri[0][0]
for  i in range(1,n):
    for j in range(i+1):
        if j!=i:
            if j!=0 and j!=i:
                temp[i][j]=max(temp[i-1][j-1],temp[i-1][j])+tri[i][j]
            else:
                temp[i][j]=temp[i-1][j]+tri[i][j]
        else:
            temp[i][j]=temp[i-1][j-1]+tri[i][j]

print(max(temp[-1]))
