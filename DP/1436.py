#BOJ - 1로 만들기

'''
DP 동적계획법
'''


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
temp = [0]*(10**6+1)
temp[1]=0
temp[2]=1
temp[3]=1
for i in range(4,n+1):
    if i%2==0 and i%3==0:
        temp[i] = min(temp[i-1]+1, temp[int(i/2)]+1, temp[int(i/3)]+1)
    elif i%3==0:
        temp[i] = min(temp[i-1]+1, temp[int(i/3)]+1)
    elif i%2==0:
        temp[i] = min(temp[i-1]+1, temp[int(i/2)]+1)
    else:
        temp[i] = temp[i-1]+1
print(temp[n])
