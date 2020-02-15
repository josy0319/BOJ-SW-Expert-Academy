#Programmers - 에상 대진표

'''
규칙성 찾기
'''

def solution(n,a,b):
    answer=1
    while True:
        if max(a,b) == min(a,b)+1 and min(a,b)&1:
            break
        a=a//2+a%2
        b=b//2+b%2
        answer+=1
    return answer
