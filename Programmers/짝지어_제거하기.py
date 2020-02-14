#Programmers - 짝지어 제거하기

'''
stack 활용
'''

def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    return 1 if len(stack)==0 else 0
