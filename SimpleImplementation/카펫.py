#Programmers - 카펫

'''
방정식
or 완전 탐색
'''


def solution(brown, red):
    for i in range(1, red//2+1):
        if red % i == 0:
            if 2*(i + red//i)+4 == brown:
                return [red//i+2, i+2]