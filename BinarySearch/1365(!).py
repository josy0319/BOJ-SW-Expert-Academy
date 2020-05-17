BOJ - 꼬인 전깃줄
 
'''
Bisect 모듈 사용(이진 탐색)
LIS문제(최장 증가 수열)
이 해결법은 최장 증가 수열의 길이만 알아내고 속도가 O(NlogN)인 방법이다. 
-> 배열에 있는 데이터는 최장 증가 수열을 만족하지 않음
'''

import bisect as bs

n = int(input())
jun = list(map(int, input().split()))
res = []

for idx, i in enumerate(jun):
    #만약 첫번째 요소이거나 배열의 마지막 값이 새로 들어오는 값보다 작다면 배열에 추가
    if idx == 0 or res[-1] < i:
        res.append(i)
    else:
        #위 조건을 만족하지 않는다면 bisect모듈을 이용해 i값의 위치를 찾는다
        #-> i값이 없다면 i보다 크면서 가장 작은 값의 위치를 반환, 그 곳에 i값을 덮어씌움
        res[bs.bisect(res,i)] = i
        
#잘라야하는 전깃줄의 수를 알아야 하기 때문에 (전체 갯수 - 최장 증가 수열의 갯수) 
print(n-len(res))
    

 
 #https://sdev.tistory.com/577 참고
