#Programmers - 쇠막대기

def solution(arrangement):
    answer = 0
    arrangement = arrangement.replace('()',"L")
    temp = []
    for i in arrangement:
        if i == 'L':
            answer += len(temp)
        elif i == '(':
            temp.append('(')
        else :
            temp.pop()
            answer += 1
    return answer
