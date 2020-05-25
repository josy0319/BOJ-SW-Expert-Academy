#Programmers - 예산

'''
이분탐색
'''

def solution(budgets, M):
    res = 0
    budgets = sorted(budgets)
    start, end = 0, max(budgets)
    while start<=end:
        temp = 0
        mid = (start+end)//2
        for i in budgets:
            if i<mid:
                temp+=i
            else:
                temp+=mid
        if temp>M:
            end=mid-1
        else:
            res = mid
            start=mid+1
    return res
