#BOJ - 말이 되고픈 원숭이

'''
BFS응용 문제
일반적인 visited설계 어려울 시,
3차원 배열 생각해보기

참고문제:14442
'''

import sys
from collections import deque

dx = [-1, 0, 1, 0, 2, 1, -1, -2, -2, -1, 1, 2]
dy = [0, 1, 0, -1, 1, 2, 2, 1, -1, -2, -2, -1]

k = int(input())
w, h = map(int,input().split())

a = [list(map(int, input().split())) for _ in range(h)]
d = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]

def bfs():
    q = deque()
    q.append((0,0,0))
    while q:
        x,y,z=q.popleft()
        j=4 if z==k else 12
        if x==h-1 and y==w-1:
            print(d[x][y][z])
            return
        for i in range(j):
            xx, yy = x+dx[i], y+dy[i]
            zz=z if i<4 else z+1
            if 0<=xx<h and 0<=yy<w and a[xx][yy]==0 and d[xx][yy][zz]==0:
                d[xx][yy][zz] = d[x][y][z]+1
                q.append((xx,yy,zz))
    print(-1)
bfs()
