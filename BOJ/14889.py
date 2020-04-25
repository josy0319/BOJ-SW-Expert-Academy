#BOJ - 스타트와 링크

'''
구현
set은 사칙 연산 가능
'''

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def solve(lst):
    global grid, res
    
    for i in lst:
        start = list(i)
        link = list(set(range(n)) - set(i))

        start_com = list(combinations(start, 2))
        link_com = list(combinations(link, 2))

        start_num = 0
        for x, y in start_com:
            start_num += grid[x][y] + grid[y][x]
        link_num = 0
        for x, y in link_com:
            link_num += grid[x][y] + grid[y][x]
        
        res = min(res, abs(start_num - link_num))


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
res = sys.maxsize
l = list(combinations(list(range(n)), n//2))
solve(l)
print(res)
