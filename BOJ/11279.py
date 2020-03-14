#BOJ - 최대 힙

'''
많은 수(천,만 단위)의 데이터를 입력받을 때,
int(input())보다 int(sys.stdin.readline())를 사용하면 시간초과를 막을 수 있다.
'''


import heapq
import sys
n = int(input())
heap = []
for _ in range(n):
    k = int(sys.stdin.readline())
    if k:
        heapq.heappush(heap, -k)
    else:
        if len(heap)!=0:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
        
