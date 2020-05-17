#BOJ - 내리막길

'''
DP + DFS
'''

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

def solve(x, y):
    if (x, y) == (m-1, n-1):
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y]=0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<m and 0<=yy<n and grid[xx][yy]<grid[x][y]:
            visited[x][y] += solve(xx, yy)
    return visited[x][y]

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1]*n for _ in range(m)]

print(solve(0, 0))

#for j in visited:
#   print(j)
       

#시간 초과
# def solve():
#     global res
#     q = deque()
#     q.append((0,0))
#     while q:
#         x, y = q.popleft()
#         # print(x,y)
#         if (x, y) == (m-1, n-1):
#             res+=1
#         for i in range(4):
#             xx = x+dx[i]
#             yy = y+dy[i]
#             if 0<=xx<m and 0<=yy<n \
#                 and grid[xx][yy]<grid[x][y]:
#                 q.append((xx,yy))
#                 visited[xx][yy]=(x,y)
