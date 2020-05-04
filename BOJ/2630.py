#BOJ - 색종이 만들기

'''
분할정복
'''

import sys

input = sys.stdin.readline

n = int(input())
grid_b = [list(map(int, input().split())) for _ in range(n)]
grid_w = [[] for _ in range(n)]
for idx, j in enumerate(grid_b):
    for k in j:
        if k==0:
            grid_w[idx].append(1)
        else:
            grid_w[idx].append(0)

w = 0
b = 0
i=2
while i<=n:
    for j in range(i-1, n, i):
        for k in range(i-1, n, i):
            if grid_b[j][k]==grid_b[j-i//2][k]== \
            grid_b[j][k-i//2]==grid_b[j-i//2][k-i//2]==i/2:
                grid_b[j][k]=grid_b[j-i//2][k]= \
                grid_b[j][k-i//2]=grid_b[j-i//2][k-i//2]=i
            
            if grid_w[j][k]==grid_w[j-i//2][k]== \
            grid_w[j][k-i//2]==grid_w[j-i//2][k-i//2]==i/2:
                grid_w[j][k]=grid_w[j-i//2][k]= \
                grid_w[j][k-i//2]=grid_w[j-i//2][k-i//2]=i
    i*=2

res_b=0
res_w=0
for j in grid_b:
    res_b+=j.count(1)
for j in grid_w:
    res_w+=j.count(1)    
    
i=2
while i<=n:
    for j in range(i-1, n, i):
        for k in range(i-1, n, i):
            if grid_b[j][k]==i:
                res_b+=1
    for j in range(i-1, n, i):
        for k in range(i-1, n, i):
            if grid_w[j][k]==i:
                res_w+=1
    i*=2
print(res_w)
print(res_b)
