#BOJ - 알고스팟

'''
BFS 응용 
덱을 appendleft를 이용하여 우선순위 큐처럼 사용

BFS라고 사이즈만큼 받아서 한번에 나아갈 필요 없다.
하나씩 pop해서 조건에 따라 나아가기.
'''

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int,input().split())
maze = []
for i in range(m):
    maze.append(list(map(int,input())))
cost = [[-1]*n for _ in range(m)]
cost[0][0] = 0

q = deque()
q.append((0,0))

while q:
    temp = q.popleft()
    for i in range(4):
        xx = temp[0] + dx[i]
        yy = temp[1] + dy[i]
        if 0<=xx<m and 0<=yy<n and cost[xx][yy]==-1:
            if maze[xx][yy] == 0:
                q.appendleft((xx,yy))
                cost[xx][yy]=cost[temp[0]][temp[1]]
            elif maze[xx][yy] == 1:
                q.append((xx,yy))
                cost[xx][yy]=cost[temp[0]][temp[1]]+1
print(cost[m-1][n-1])
