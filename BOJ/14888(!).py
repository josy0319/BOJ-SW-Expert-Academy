#BOJ - 연산자 끼워넣기

'''
백트래킹
'''

import sys
from collections import deque
input = sys.stdin.readline

def solve(num, idx, add, sub, mul, div):
    global mx, mn
    if idx == n:
        mx = max(mx, num)
        mn = min(mn, num)
        return
    else:
        if add:
            solve(num+num_list[idx], idx+1, add-1, sub, mul, div)
        if sub:
            solve(num-num_list[idx], idx+1, add, sub-1, mul, div)
        if mul:
            solve(num*num_list[idx], idx+1, add, sub, mul-1, div)
        if div:
            solve(int(num/num_list[idx]), idx+1, add, sub, mul, div-1)


n = int(input())
num_list = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
mx = -sys.maxsize
mn = sys.maxsize
solve(num_list[0], 1, a, b, c, d)
print(mx)
print(mn)
