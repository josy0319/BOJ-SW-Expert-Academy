#BOJ - 포도주 지식

'''
DP 동적계획법
'''


import sys

input = sys.stdin.readline

n = int(input())
q = [int(input()) for _ in range(n)]
if n == 1:
    print(q[0])
    sys.exit(0)
elif n == 2:
    print(q[0] + q[1])
    sys.exit(0)
elif n == 3:
    print(max(q[0]+q[1], q[1]+q[2], q[0]+q[2]))
    sys.exit(0)
else:
    res = [[0]*2 for _ in range(n)]
    res[0][0] = q[0]
    res[1][0] = q[1]
    res[1][1] = q[0]+q[1]

    for i in range(2,n):
        res[i][0]=max(res[i-2][1]+q[i], res[i-2][0]+q[i], 
        res[i-3][1]+q[i], res[i-3][0]+q[i])  
        res[i][1]=max(q[i]+q[i-1], res[i-1][0]+q[i])
    print(max(res[-1])) if max(res[-1]) > max(res[-2]) else print(max(res[-2]))
