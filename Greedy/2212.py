#BOJ - 센서

'''
그리디(Greedy)
'''

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

l = []
for i in range(1, n):
    l.append(sensor[i]-sensor[i-1])
l.sort()
for j in range(k-1):
    if len(l)==0:
        l.append(0)
        break
    else:
        l.pop()
print(sum(l))

