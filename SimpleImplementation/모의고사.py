#Programmers - 모의고사

'''
완전탐색
'''

def solution(answers):
    res = []
    score = [0] * 3
    first = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if(first[i%5] == answers[i]):
            score[0]+=1
        if(sec[i%8] == answers[i]):
            score[1]+=1
        if(third[i%10] == answers[i]):
            score[2]+=1
    for idx, i in enumerate(score):
        if max(score)==i:
            res.append(idx+1)
    return res