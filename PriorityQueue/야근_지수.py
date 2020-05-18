#Programmers - 야근 지수

'''
PriorityQueue
heap

heapify한번 보다, 
heappop, heappush한번씩 하는게 효율적이다.
'''

import heapq as hq
def solution(n, works):
    res = 0
    for i in range(len(works)):
        works[i]*=-1
    hq.heapify(works)
    while n>0:
        m = hq.heappop(works)
        if m >= 0:
            return 0
        m += 1
        hq.heappush(works, m)
        n-=1
    for i in works:
        if i>0:
            return 0
        res+=i**2
    return res if res>0 else -res
