#BOJ - N번째 큰 수

'''
우선순위 큐

시간복잡도와 공간복잡도 모두 만족해야함.
'''



import sys
import heapq as h
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
h.heapify(num)

for _ in range(n-1):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in temp:
        if i > num[0]:
            h.heappush(num,i)
            h.heappop(num)

print(num[0])
