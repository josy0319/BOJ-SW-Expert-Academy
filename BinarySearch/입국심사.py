#Programmers - 입국심사

'''
이분탐색
'''


def solution(n, times):
    res = 0
    times = sorted(times)
    start, end = 0, n*max(times)
    while start<=end:
        temp = 0
        mid = (start+end)//2
        for i in times:
            temp+=mid//i  
        if temp>=n:
            res=mid
            end=mid-1
        else:
            start=mid+1
    return res
