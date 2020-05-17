#BOJ - 나무 자르기

'''
이분탐색
end값을 응용
'''


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree)

while start<=end: 
    mid = (start+end)//2
    res = 0
    for i in tree:
        if i>mid:
            res+=(i-mid)
    if res<m:
        end=mid-1
    if res>=m:
        start=mid+1
print(end)
