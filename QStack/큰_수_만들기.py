#Programmers - 큰 수 만들기

'''
탐욕법(Greedy)
stack구조 활용
시간 초과 날 때는 pop대신 index를 사용하자
'''

def solution(number, k):
    answer = ''
    number = list(map(int,number))
    stack = []
    cnt = 0
    while cnt < len(number):
        if stack and stack[-1] < number[cnt] and k>0:
            stack.pop()
            k-=1
        else:
            stack.append(number[cnt])
            cnt += 1
    if k != 0:
        return answer.join(map(str,stack[:-k]))
    else:
        return answer.join(map(str,stack))
