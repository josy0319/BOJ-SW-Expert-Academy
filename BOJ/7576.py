#BOJ - 토마토

'''
BFS
'''

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
m, n = map(int,input().split())
t = [[] for _ in range(n)]
visited = [[0]*m for _ in range(n)]
for i in range(n):
    t[i] = list(map(int,input().split()))
box = deque()

for i in range(n):
    for j in range(m):
        if t[i][j] == 1:
            box.append((i,j))
res = 0
while box:
    size = len(box)
    for i in range(size):
        temp = box.popleft()
        for j in range(4):
            xx = temp[0] + dx[j]
            yy = temp[1] + dy[j]
            if 0<=xx<n and 0<=yy<m and t[xx][yy] == 0:
                box.append((xx,yy))
                t[xx][yy] = 1
    res+=1
cnt = 0
for i in t:
    cnt += i.count(0)
print(res-1) if cnt == 0 else print(-1)
