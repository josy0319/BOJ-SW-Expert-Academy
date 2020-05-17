#programmers - 프린터
def solution(priorities, location):
    answer = 0
    temp = [0] * len(priorities)
    temp[location] = 1
    total=0
    for i in range(0,len(priorities)):
        for k in range(0,len(priorities)):
            for j in range(1,len(priorities)):
                if priorities[0] < priorities[j] : 
                    a = priorities.pop(0)
                    priorities.append(a)
                    b = temp.pop(0)
                    temp.append(b)                    
                    break
        a=priorities.pop(0)
        b=temp.pop(0)
        total += 1
        if(b==1):
            answer = total
            break
    return answer
