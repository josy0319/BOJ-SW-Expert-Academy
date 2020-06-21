# BOJ - 해킹

'''
다익스트라
그래프 문제
'''

import sys
import heapq as hq

input=sys.stdin.readline

def dijkstra(start):
    heap = []
    # weight와 시작 node 초기화
    hq.heappush(heap, [0, start])
    # 다익스트라를 위한 max 배열 생성 
    dp = [float('inf') for _ in range(n+1)]
    # 시작 값 초기화
    dp[start] = 0
    while heap:
        start_weight, start_node = hq.heappop(heap)
        # 목표 노드의 값 순회
        for des_node, des_weight in s[start_node]:
            # 이동 값이 더 작은 경우
            weight = start_weight+des_weight
            if dp[des_node]>weight:
                # 작은 값으로 치환해주고
                dp[des_node]=weight
                # 힙에 값과 노드 push
                hq.heappush(heap, [weight, des_node])
    return dp

for _ in range(int(input())):
    n, d, start = map(int, input().split())
    # 리스트로 받을 배열 생성
    s = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, c = map(int, input().split())
        # 그래프 형식으로 연결 값과 weight 저장
        s[b].append([a, c])

    dp = dijkstra(start)
    max_dp = 0
    cnt = 0
    for i in dp:
        if i != float('inf'):
            if max_dp < i:
                max_dp = i
            cnt += 1
    print(cnt, max_dp)
