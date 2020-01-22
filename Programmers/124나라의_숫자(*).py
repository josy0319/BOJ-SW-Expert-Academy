#Programmers - 124나라의 숫자

def solution(n):
    answer = ""
    while n > 0:     
        answer = "412"[n%3] + answer
        n = (n-1) // 3      
    return answer
