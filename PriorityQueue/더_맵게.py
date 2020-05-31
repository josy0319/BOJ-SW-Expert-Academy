#Programmers - 더 맵게

'''
PriorityQueue
heap
'''

import heapq as hq
def solution(scoville, K):
    res=0
    hq.heapify(scoville)
    while True:
        x = hq.heappop(scoville)
        if x>=K:
            break
        try:
            y = hq.heappop(scoville)
            hq.heappush(scoville, x+y*2)
            res+=1
        except:
            return -1
    return res