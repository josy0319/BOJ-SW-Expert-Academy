#Programmers - 튜플

'''
단순 구현
'''


def solution(s):
    res = []
    s = [i.replace('{', '') for i in s.split(',')]
    s = sorted([int(i.replace('}', '')) for i in s])
    d = dict()
    for i in s:
        if d.get(i)!=None:
            d[i] = d.get(i)+1
        else:
            d[i] = 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in d:
        res.append(i[0])
    return res
