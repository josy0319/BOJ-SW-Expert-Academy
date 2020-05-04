#BOJ - 쿼드트리

'''
분할정복
'''

import sys

input = sys.stdin.readline

def solve(x, y, N):
    color = grid[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != grid[i][j]:
                print('(', end='')
                solve(x, y, N//2)
                solve(x, y+N//2, N//2)
                solve(x+N//2, y, N//2)
                solve(x+N//2, y+N//2, N//2)
                print(')', end='')
                return
    print(str(color), end='')

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
solve(0, 0, n)
