#BOJ - 신입 사원

'''
그리디(Greedy)
'''

import sys

input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    l=[list(map(int, input().split())) for _ in range(n)]
    res=1
    #a는 높을수록 좋고, b는 낮을수록 좋음
    #순위는 동석차 없음
    l.sort(key=lambda x:(x[1]))
    temp=l[0][0]
    for i in range(1, len(l)):
        if temp>=l[i][0]:
            res+=1
            temp=l[i][0]
    print(res)


#1차시기
'''
for _ in range(int(input())):
    n=int(input())
    l=[list(map(int, input().split())) for _ in range(n)]
    res=1
    #a는 높을수록 좋고, b는 낮을수록 좋음
    #순위는 동석차 없음
    l.sort(key=lambda x:(x[1]))
    print(l)
    for i in range(1, len(l)):
        for j in range(i):
            # print(i, j)
            if l[i][0]>l[j][0]:
                break
        else:
            res+=1
    print(res)
'''

