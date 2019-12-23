#programmers - 기능개발

import math
def solution(progresses, speeds):
    answer = []
    result = []
    for i in range(len(progresses)):
        temp = 100 - progresses[i]
        score = math.ceil(temp / speeds[i])
        result.append(score)
    for i in range(len(result)):
        total = 1
        flag = 1 
        for j in range(i+1,len(result)):
            if result[i] >= result[j] and flag == 1:
                total+=1
                result[j]=-1
            else: 
                flag = 0
                break
        if result[i] != -1:
            answer.append(total)
    return answer
