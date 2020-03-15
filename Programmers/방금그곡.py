#Programmers - 방금그곡

'''
코드 구현력
'''


def solution(m, music):
    res = []
    result = []
    cnt = -1
    for j in range(len(m)):
            if '#' not in m:
                break
            if m[j] == '#':
                m = m.replace(m[j-1]+'#', m[j-1].lower())
    for i in music:
        start, end, name, um  = i.split(',')
        start, end= start.split(':') , end.split(':')
        ing = (int(end[0])-int(start[0]))*60 + (int(end[1])-int(start[1]))
        
        for j in range(len(um)):
            if '#' not in um:
                break
            if um[j] == '#':
                um = um.replace(um[j-1]+'#', um[j-1].lower())
        total_um = ''
        cnt = ing
        while True:
            if len(um) <= cnt:
                total_um += um
                cnt -= len(um)
            else:
                total_um += um[:cnt]
                break
        res.append((total_um, name, ing))
    for i in res:
        if m in i[0]:
            result.append((i[1],i[2]))
    if len(result) == 0:
        return '(None)'
    result = sorted(result, key=lambda x:-x[1])
    return result[0][0]
