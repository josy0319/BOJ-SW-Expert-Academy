#BOJ - 암호 만들기

'''
combinations 활용
'''


import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
alpha = list(sys.stdin.readline().split())
alpha.sort()
#print(alpha)
#암호는 최소 한개의 모음과 최소 두개의 자음으로 구성
mo = ['a', 'e', 'i', 'o', 'u']
res = combinations(alpha,l)
for i in (res):
    cnt = 0
    for j in mo:
        cnt += i.count(j)
    if 0 < cnt <= l-2:
        #print(cnt)
        print(''.join(i))
    
