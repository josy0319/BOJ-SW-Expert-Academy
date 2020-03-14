# BOJ - 카드 정렬하기

'''
우선 순위 큐
'''


import sys
import heapq

n = int(sys.stdin.readline())
heap = []
res = 0
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))
while heap:
    if len(heap) >= 2:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        heapq.heappush(heap,a+b)
        res+=a+b
    else:
        if res == 0 and heap[0] == 1:        
            res = 0
            heapq.heappop(heap)
        elif res == 0:
            res = heapq.heappop(heap)

        else:
            break
print(res)
