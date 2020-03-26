#BOJ - 구슬 탈출(삼성기출)

'''
BFS 응용
'''


import sys
from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def move(x,y,dx,dy):
    count=0
    while board[x+dx][y+dy]!='#' and board[x][y]!='O':
        x+=dx
        y+=dy
        count+=1
    return x,y,count

def bfs():
    global dy
    q=deque()
    q.append((r[0],r[1],b[0],b[1],1))
    while q:
        temp = q.popleft()
        if temp[4]>10:
            break
        for i in range(4):
            rx, ry, r_cnt=move(temp[0],temp[1],dx[i],dy[i])
            bx, by, b_cnt=move(temp[2],temp[3],dx[i],dy[i])

            if board[bx][by]=='O':
                continue
            if board[rx][ry]=='O':
                print(1)
                return
            if bx==rx and by==ry:
                if b_cnt>r_cnt:
                    bx-=dx[i]
                    by-=dy[i]
                else:
                    rx-=dx[i]
                    ry-=dy[i]
            if visited[rx][ry][bx][by]==0:
                visited[rx][ry][bx][by]=1
                q.append((rx,ry,bx,by,temp[4]+1))
    print(0)
    

n, m = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range (n)]
visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
#visited 딕셔너리(아이디어)
==
for i in range(n):
    for j in range(m):
        if board[i][j]=='B':
            b=(i,j)
        if board[i][j]=='R':
            r=(i,j)
visited[r[0]][r[1]][b[0]][b[1]]=1
bfs()
