#Programmers - 호텔 방 배정

'''
defaultdict 활용
union-find 활용 

리스트로는 못푸는 문제 -> 10**12
'''

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

parent = defaultdict(int)

def find(num):
    if parent[num]==0:
        return num
    if parent[num]!=num:
        parent[num]=find(parent[num])
    return parent[num]
    
def solution(k, room):
    res = []
    for i in room:
        x = find(i)
        res.append(x)
        parent[x] = find(x+1)
        parent[i] = parent[x]
    return res
