#Programmers - 실패율

'''
딕셔너리 정렬
딕셔너리의 items로 값 가져온 후 key를 통해 람다식
[0] -> key값 기준 정렬
[1] -> value값 기준 정렬
'''

def solution(n, s):
    res = []
    temp = {}
    cnt = len(s)
    for i in range(1,n+1):
        if cnt == 0:
            temp[i] = 0
        else:
            temp[i] = s.count(i)/cnt
            cnt -= s.count(i)
    for i in sorted(temp.items(),key= lambda x:x[1], reverse=True):
        res.append(i[0])
    return res
