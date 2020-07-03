#BOJ - 뒤집기


import sys
from collections import Counter

input = sys.stdin.readline

s = input()
temp = ''
result = ''
for i in s:
    if temp==i:
        continue
    else:
        result+=i
        temp=i
print(Counter(result)['0']) if Counter(result)['0']<Counter(result)['1'] else print(Counter(result)['1'])
