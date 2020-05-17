#Programmers - 숫자 야구

'''
DFS
완전 탐색
중복 순열 이용
'''


def DFS(L,predict,b):
    global temp
    if L == 3:
        for i in b:
            strike = 0
            ball = 0
            for j in range(3):
                #스트라이크 조건
                if str(i[0])[j] == predict[j]:
                    strike += 1
                for k in range(3):
                    #볼 조건
                    if str(i[0])[j] == predict[k]:
                        ball += 1
            if i[1] == strike:
                if i[2] == ball - strike:
                    if predict[0] != predict[1] and predict[1] != predict[2] and predict[0] != predict[2]:
                        temp.append(predict) 
                        
    else:
        for i in range(1,10):
            DFS(L+1,predict+str(i),b)

def solution(b):
    global temp
    answer = 0
    predict = ''
    temp = []
    DFS(0,predict,b)
    for i in temp:
        if temp.count(i) == len(b):
            answer += 1
    return answer//len(b)
