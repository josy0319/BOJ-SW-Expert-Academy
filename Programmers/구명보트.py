#Programmers - 구명보트

'''
효율성 고려
시간복잡도 -> 리스트에서 빼는 행위 지양
'''

#1차시기 -> 효율성 고려 못하고 deque으로 풀어서 정답은 맞았으나 효율성에서 실패 
from collections import deque
def solution(people, limit):
    res = 0
    people.sort()
    q = deque(people)
    while q:
        if q[-1]+min(q) > limit:
            q.pop()
            res+=1
        else:
            if len(q) >= 2:
                if q[0] + q[-1] <= limit:
                    q.popleft()
                    q.pop()
                    res+=1
            else:
                q.pop()
                res+=1
                break
    return res

#2차시기 -> 지문을 다시 읽고 간단한 방법으로 전환
def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)-1
    res = 0
    while start <= end:
        res += 1
        if people[start] + people[end] <= limit:
            start +=1
        end-=1
    return res
