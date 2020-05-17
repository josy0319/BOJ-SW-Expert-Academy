#BOJ - 숨바꼭질

'''
DFS, BFS 함수 구현을 습관화

함수 구현하지 않고 break걸면 -> 런타임에러
함수화하고 return걸면 -> 통과
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            print(visited[x])
            return
        for i in range(3):
            if dx[i] == 2:
                xx=x*2
            else:
                xx=x+dx[i]
            if 0<=xx<100001 and visited[xx]==0:
                q.append(xx)
                visited[xx]=visited[x]+1

n, k = map(int, input().split())
visited = [0]*100001
dx = [1, -1, 2]
bfs()
