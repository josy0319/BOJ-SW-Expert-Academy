#BOJ - 나이트의 이동

'''
BFS
'''


from collections import deque
import sys

dx=[-1,-1,1,1,-2,-2,2,2]
dy=[2,-2,2,-2,1,-1,1,-1]

for _ in range(int(sys.stdin.readline())):
    l = int(input())
    x1,y1=map(int,sys.stdin.readline().split())
    x2,y2=map(int,sys.stdin.readline().split())
    visited=[[0]*l for _ in range(l)]
    visited[x1][y1]=0
    depth=0

    q=deque()
    q.append((x1,y1,depth))
    while q:
        temp=q.popleft()
        if temp[:2]==(x2,y2):
            print(visited[temp[0]][temp[1]])
            break
        for i in range(8):
            xx=temp[0]+dx[i]
            yy=temp[1]+dy[i]
            if 0<=xx<l and 0<=yy<l and visited[xx][yy]==0:
                visited[xx][yy]=temp[2]+1
                q.append((xx,yy,temp[2]+1))
