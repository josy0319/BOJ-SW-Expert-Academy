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



if __name__=="__main__":
    n = list(input())
    res = 0
    #res는 막대기 값
    i, cnt = 0, 0
    #i는 순차적으로 검사하는 인덱스
    #cnt는 누적된 (의 갯수
    while i < len(n):
        temp = n[i]
        #(만 나와서 +=1해야되는 경우
        if temp == '(':
            if n[i+1] != ')':
                cnt += 1
                res += 1
            else:
                cnt +=  1
        #()가나와서 쏘는 경우
        elif temp == ')' and n[i-1] == '(':
            if cnt > 1:
                cnt -= 1
                res += cnt
            else:
                cnt = 0
        #)만 나오는 경우
        elif temp == ')':
            cnt -= 1
        i+=1
    print(res)
