#Programmers - 불량_사용자

'''
정규 표현식 응용
dfs
'''

import re
def solve(L, s):
    global result, banned_length, temp
    if L==banned_length:
        result.add(tuple(sorted(s)))
    else:
        for i in range(len(temp[L])):
            if temp[L][i] not in s:
                s.append(temp[L][i])
                solve(L+1, s)
                s.pop()
def solution(user, banned):
    global banned_length, result, temp
    banned_length=len(banned)
    temp = [[] for _ in range(len(banned))]
    result = set()
    for idx, i in enumerate(banned):
        i = '^{}$'.format(i.replace('*', '.'))
        for j in user:
            p = re.findall(i, j)
            if len(p)!=0:
                temp[idx].append(''.join(p))
        temp[idx] = list(set(temp[idx]))
    solve(0, [])
    return len(result)
