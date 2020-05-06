#BOJ - 0만들기

'''
backtracking
'''

import sys

input = sys.stdin.readline

#op==2 시작
#op==1 -
#op==0 +
def solve(L, l, num, s, op):
    if L==n:
        if num==0:
            print(s)
        return
    else:
        if op==2 or op==0:
            solve(L+1, (10*l)+(L+1), num+((10*l)+(L+1))-l, s+' '+str(L+1), 0)
        if op==1:
            solve(L+1, (10*l)+(L+1), num-((10*l)+(L+1))+l, s+' '+str(L+1), 1)
        solve(L+1, L+1, num+(L+1), s+'+'+str(L+1), 0)
        solve(L+1, L+1, num-(L+1), s+'-'+str(L+1), 1)

for _ in range(int(input())):
    n = int(input())
    solve(1, 1, 1, '1', 2)
    print()
