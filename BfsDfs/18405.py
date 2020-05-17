#BOJ - 경쟁적 감염

'''
BFS
'''

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#낮은 번호부터 증식
def solve():
    q = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j]!=0:
                q.append((grid[i][j], i, j, 0))
    q = deque(sorted(q))
    while q:
        temp = q.popleft()
        if temp[3]==s:
            print(grid[x-1][y-1])
            return
        for i in range(4):
            xx = temp[1]+dx[i]
            yy = temp[2]+dy[i]
            if 0<=xx<n and 0<=yy<n and grid[xx][yy]==0:
                grid[xx][yy]=temp[0]
                q.append((temp[0], xx, yy, temp[3]+1))
    else:
        print(grid[x-1][y-1])
    
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
solve()

