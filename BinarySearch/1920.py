#BOJ - 수 찾기

'''
이분탐색
'''


import sys
input = sys.stdin.readline

n = int(input())
nl = sorted(list(map(int, input().split())))
m = int(input())
ml = list(map(int, input().split()))
res=0
for i in ml:
    start = 0
    end = len(nl)-1
    while start<=end:
        mid = (start+end)//2
        if nl[mid]==i:
            print(1)
            break
        if nl[mid]>i:
            end=mid-1
        else:
            start=mid+1
    else:
        print(0)
