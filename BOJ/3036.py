#BOJ - 링


import sys

input = sys.stdin.readline

n = int(input())
ring = list(map(int, input().split()))
fr = ring.pop(0)

for i in ring:
    temp=0
    if i<fr:
        for j in range(i,0,-1):
            if i%j==0 and fr%j==0:
                temp=j
                break
    else:
        for j in range(fr,0,-1):
            if i%j==0 and fr%j==0:
                temp=j
                break
    print('{}/{}'.format(int(fr/j), int(i/j)))
