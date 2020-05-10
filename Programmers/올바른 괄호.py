#Programmers - 올바른 괄호

'''

'''


def solve(s, x, y):
    global res
    if y<x:
        return
    if (x, y) == (0, 0):
        while '()' in s:
            s=s.replace('()', '')
        if s=='':
            res+=1
    else:
        if x>0:
            solve(s+'(', x-1, y)
        if y>0:
            solve(s+')', x, y-1)
def solution(n):
    global res
    res = 0
    solve('', n, n)
    return res
