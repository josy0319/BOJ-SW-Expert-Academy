import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

for i in s:
    rank=1
    for j in s:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank, end=' ')
