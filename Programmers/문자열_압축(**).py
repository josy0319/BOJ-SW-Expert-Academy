#Programmers - 문자열 압축
#깔끔하고 간결하게 풀 수 있도록 노력하기

def solution(s):
    if len(s) < 3:
        answer = len(s)
    
    answer = len(s)
    max_cand = int(len(s)/2)
    for interval in range(1,max_cand+1):
        start = interval
        result = []
        pre = s[0:interval]
        num = 1
        while True:
            now = s[start:start+interval]
            if now == pre:
                num += 1
            else:
                result.append([num,pre])
                num = 1
                pre = now
            if start > len(s):
                break
            start += interval
        len_card = 0
        for k in range(len(result)):
            if result[k][0] == 1:
                len_card += len(result[k][1])
            else:
                len_card += len(str(result[k][0]))
                len_card += len(result[k][1])
        answer = min(answer,len_card)
    return answer
