#Programmers - 라면공장

'''
@heapq의 사용법
파이썬에서의 heapq모듈은 기본적으로 min-heap을 지원한다.
max-heap을 사용하려면 (-기본값, 기본값)의 튜플 형식으로 heappush를 해준 후
pop을 해야하는 경우 [1]을 사용하여 max-heap으로 정렬된 값을 pop해주도록 한다.

우선 순위가 정해져있고 리스트를 써야하는 경우 heapq 모듈을 고려,
시간적으로 우위에 있음
'''


#1차 시기 -> heap사용 안하고 오로지 리스트만 사용한 경우 -> 효율성 실패
def solution(stock, dates, supplies, k):
    res = 0
    temp = []
    cnt = 0
    for i in range(k):
        if stock >= k-i:
            break
        if i in dates:
            temp.append(supplies[cnt])
            cnt+=1
        if stock == 0:
            stock += supplies[supplies.index(max(temp))]
            supplies[supplies.index(max(temp))] = -1
            temp[temp.index(max(temp))] = -1
            res += 1
        stock -= 1
    return res

#2차 시기 -> 우선순위 큐 돌입, 위 방법과 비슷하게 heap으로만 대체 -> 시간 살짝 단축되었으나 효율성 실패
import heapq
def solution(stock, dates, supplies, k):
    res = 0
    heap = []
    cnt = 0
    for i in range(k):
        if stock > k-i:
            break
        if i in dates:
            heapq.heappush(heap, (-supplies[cnt],supplies[cnt]))
            cnt+=1
        if stock == 0:
            stock += heapq.heappop(heap)[1]
            res += 1
        stock -= 1
    return res

#3차 시기 -> 우선 순위 큐 + 로직 변경 -> 시간 많이 단축 + 효율성 성공
import heapq
def solution(stock, dates, supplies, k):
    res = 0
    heap = []
    cnt = 0
    while stock<k:
        for i in range(cnt,len(dates)):
            if dates[cnt] <= stock:
                heapq.heappush(heap,(-supplies[i],supplies[i]))
                cnt += 1
            else:
                break
        stock += heapq.heappop(heap)[1]
        res+=1
    return res
