#Programmers - 소수 만들기

'''
itertools의 combinations활용
'''


from itertools import combinations
def solution(nums):
    answer = 0
    s = list(combinations(nums,3))
    for i in s:
        cnt = 0
        for j in range(2,sum(i)):
            if sum(i) % j == 0 :
                cnt+=1
        if cnt < 1:
            answer += 1
    return answer
