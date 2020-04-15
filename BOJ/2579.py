#BOJ - 계단 오르기

'''
DP 동적계획법
'''

import sys

input = sys.stdin.readline

n = int(input())
flr = [int(input()) for _ in range(n)]
if n==1:
    print(flr[0])
    sys.exit(0)
else:
    temp = [[0]*3 for _ in range(n)]
    temp[0][1], temp[1][1], temp[1][2] = flr[0], flr[1], flr[0]+flr[1]

    i=2
    while i<n:
        for j in range(3):
            if j==1:
                temp[i][j]=max(temp[i-2][0], temp[i-2][1], temp[i-2][2] \
                ) + flr[i]
                    
            elif j==2:
                if temp[i-1][1]!=0:
                    temp[i][j]=temp[i-1][1] + flr[i]
        i+=1
    print(max(temp[-1]))
