# BOJ - 거의 최단 경로

'''
다익스트라 응용
그래프 문제
'''

import sys
import heapq as hq
from collections import deque

input = sys.stdin.readline

def dijkstra(start):
    heap = []
    hq.heappush(heap, [0, start])
    score = [float('inf') for _ in range(n)]
    score[start] = 0
    while heap:
        start_weight, start_node = hq.heappop(heap)
        for des_node, des_weight in info[start_node]:
            weight = start_weight+des_weight
            if weight<score[des_node] and check[start_node][des_node]==0:
                score[des_node]=weight
                hq.heappush(heap, [weight, des_node])
    return score

def delete(end, dp):
    q = deque()
    # 도착점으로부터 출발점까지의 최단경로를 찾음
    q.append(end)
    while q:
        node = q.popleft()
        for des_node, des_weight in info_[node]:
            # 최단경로 weight과 동일하다면,
            if dp[node] == dp[des_node]+des_weight:
                # check하여 다익스트라 호출시 최단경로 무시
                check[des_node][node]=1
                q.append(des_node)

while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    else:
        s, d = map(int, input().split())
        # 출발점 to 도착점
        info = [[] for _ in range(n+1)]
        # 도착점 to 출발점
        info_ = [[] for _ in range(n+1)]
        # 최단경로 제외를 위한 check 배열
        check = [[0]*n for _ in range(n)]
        for _ in range(m):
            #u, v, p / 시작점, 도착점, 가중치
            u, v, p = map(int, input().split())
            info[u].append([v, p])
            info_[v].append([u, p])
        dp = dijkstra(s)
        # print(dp)
        delete(d, dp)
        # print(check)
        dp = dijkstra(s)
        print(dp[d]) if dp[d]!=float('inf') else print(-1)
