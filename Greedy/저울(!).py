#Programmers - 저울

'''
그리디 탐욕법
수학적 접근 필요
'''

def solution(weight):
    res = 1
    w = sorted(weight)
    for i in w:
        if res<i:
            break
        res+=i
    return res

