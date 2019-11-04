#완주하지_못한_선수(Programmers)

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(0,len(participant)-1):
        if(participant[i] != completion[i]):
            answer = participant[i]
            break
        else :
            answer = participant[-1]
    return answer
