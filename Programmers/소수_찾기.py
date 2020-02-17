#Programmers - 소수 찾기

'''
set자료형에서 |= 통해 합집합 활용
비트연산자
'''

#코드 정리 전
from itertools import permutations
def solution(numbers):
    res = set()
    n = list(map(int,numbers))
    for i in range(1,len(n)+1):
        case = permutations(n,i)
        for j in case:
            res.add(j)
    temp = set()
    for i in res:
        a=''
        for j in i:
            a+=str(j)
        temp.add(int(a))
    result = 0
    for i in temp:
        cnt = 0
        for j in range(1,i//2+1):
            if i%j==0:
                cnt += 1
        if cnt < 2 and i != 0 and i != 1:
            result += 1
    return result
    
    
#소스 정리 후
from itertools import permutations
def solution(n):
    res = set()
    for i in range(len(n)):
        res |= set(map(int, map("".join, permutations(list(n), i + 1))))
    result = 0
    for i in res:
        cnt = 0
        for j in range(1,i//2+1):
            if i%j==0:
                cnt += 1
        if cnt < 2 and i != 0 and i != 1:
            result += 1
    return result
