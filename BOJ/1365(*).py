 #BOJ - 꼬인 전깃줄
 
'''
Bisect 모듈 사용(이진 탐색)
LIS문제(최장 증가 수열)
이 해결법은 최장 증가 수열의 길이만 알아내고 속도가 O(NlogN)인 방법이다. 
-> 배열에 있는 데이터는 최장 증가 수열을 만족하지 않음

#https://sdev.tistory.com/577 참고
'''

import bisect as bs

n = int(input())
jun = list(map(int, input().split()))
res = []

for idx, i in enumerate(jun):
    if idx == 0 or res[-1] < i:
        res.append(i)
    else:
        res[bs.bisect(res,i)] = i
    print(res)
print(n-len(res))
    

