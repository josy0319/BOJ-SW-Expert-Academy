#Programmers - 숫자의 표현

def solution(n):
    answer = 0
    temp = list(range(1,n+1))
    x,y =0 ,1
    while True:
        if x == n-1:
            break
        if sum(temp[x:y]) < n:
            y+=1
        elif sum(temp[x:y]) == n:
            x+=1
            y=x+1
            answer+=1
        else:
            x+=1
            y=x+1
    return answer+1
