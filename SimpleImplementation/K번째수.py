#K번째수(Programmers)

def solution(array, commands):
    answer = []
    for i in range(0,len(commands)) :
        answer1 = array[commands[i][0]-1:commands[i][1]]
        answer1.sort()
        answer.append(answer1[commands[i][2]-1])
        del(answer1)
        
    return answer
