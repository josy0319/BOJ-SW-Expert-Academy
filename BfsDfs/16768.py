#BOJ - Mooyo Mooyo

'''
뿌요뿌요 로직
DFS 사용
'''


import sys
from collections import deque
from itertools import chain
from copy import deepcopy

input = sys.stdin.readline

dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<10 and grid[xx][yy]==grid[x][y] and \
            check[xx][yy]==0 and grid[xx][yy]!=0:
            check[xx][yy]=1
            dfs(xx, yy)

def logic():
    for i in range(n-1, -1, -1):
        for j in range(10):
            if grid[i][j]!=0:
                dfs(i, j)
                if sum(list(chain(*check)))>=k:
                    for x in range(n-1, -1, -1):
                        for y in range(10):
                            if check[x][y]==1:
                                check[x][y]=0
                                grid[x][y]=0
                else:
                    for x in range(n-1, -1, -1):
                        for y in range(10):
                            if check[x][y]==1:
                                check[x][y]=0

def sort_grid():
    for _ in range(n-1):
        for i in range(10):
            for j in range(n-1, -1, -1):
                if grid[j][i]==0:
                    for k in range(j-1, -1, -1):
                        if grid[k][i]!=0:
                            grid[j][i]=grid[k][i]
                            grid[k][i]=0
                        break

n, k = map(int, input().split())
grid = list(list(map(int, input()[:-1])) for _ in range(n))
check = list([0]*10 for _ in range(n))

while True:
    logic()
    first_grid = deepcopy(grid)
    sort_grid()
    second_grid = deepcopy(grid)
    if first_grid==second_grid:
        break
for i in grid:
    for j in i:
        print(j, end='')
    print()
        
