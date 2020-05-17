#Programmers - 캐시

'''
stack활용
LRU 알고리즘
'''

def solution(cacheSize, cities):
    res = 0
    c = [x.lower() for x in cities ]
    s = []
    for i in range(len(c)):
        if c[i] in s:
            res += 1
            s.append(s.pop(s.index(c[i])))
        else:
            res += 5
            if cacheSize == 0:
                return len(c)*5
            else:
                if len(s) == cacheSize:
                    s.pop(0)
                    s.append(c[i])
                else:
                    s.append(c[i])
    return res
