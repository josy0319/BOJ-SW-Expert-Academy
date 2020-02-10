#Programmers - 올바른 괄호

def solution(s):
    cnt = 1
    if s[0] == ')' or s[-1] == '(':
        return False
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return False
    if cnt > 1 :
        return False
    else:
        return True
