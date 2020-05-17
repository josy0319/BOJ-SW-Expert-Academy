#Programmers - 뉴스 클러스터링

'''
list comprehension
합집합, 교집합 활용
'''

def solution(str1, str2):
    answer = 0
    s1 = [str1[i-2:i].lower() for i in range(2,len(str1)+1,1) if str1[i-2:i].isalpha()]
    s2 = [str2[i-2:i].lower() for i in range(2,len(str2)+1,1) if str2[i-2:i].isalpha()]
    if len(s1) == 0 and len(s2) == 0:
        return 65536
    else:
        it_cnt = 0
        for i in range(len(s1)):
            if s1[i] in s2:
                s2[s2.index(s1[i])] = -1
                it_cnt +=1
        u_cnt = len(s1) + len(s2) - it_cnt
    return int(it_cnt/u_cnt*65536)
