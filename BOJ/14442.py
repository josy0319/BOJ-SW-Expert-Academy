#BOJ - 벽 부수고 이동하기

'''
BFS 응용문제
visited과 cnt역할을 하는 3차원 배열을 활용
'''


import sys
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    q=deque()
    q.append((0,0,0))

    while q:
        x,y,z = q.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if (x,y)==(n-1,m-1):
                print(visited[x][y][z])
                return
            if 0<=xx<n and 0<=yy<m and visited[xx][yy][z]==0:
                if board[xx][yy]==0:
                    visited[xx][yy][z]=visited[x][y][z]+1
                    q.append((xx,yy,z))
                elif board[xx][yy]==1 and z<k:
                    visited[xx][yy][z+1]=visited[x][y][z]+1
                    q.append((xx,yy,z+1))
    print(-1)

n, m, k = map(int, sys.stdin.readline().split())
board = [list(map(int,input())) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1

bfs()


