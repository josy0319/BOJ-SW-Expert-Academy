#[3차] 파일명 정렬
#정규식 응용과 리스트의 sorted, lambda사용

import re
def solution(files):
    answer = []
    temp = []
    p = re.compile('([A-Za-z.-]+)(\d+)(.*)')
    #정규식 표현법
    for i in files:
        m = p.match(i)
        temp.append([m.group(1), m.group(2), m.group(3)])
        #정규식에서 ()사용시 group으로 나눠 사용 가능
    
    #int해주는 이유 -> 10 < 0011 < 012 < 13 < 014이기 때문에 int
    temp = sorted(temp, key = lambda x:int(x[1]))
    temp = sorted(temp, key = lambda x:x[0].lower())
    #x[0]을 우선 정렬해야 하기 때문에 나중에 정렬한다.
    
    for i in temp:
        answer.append(i[0]+i[1]+i[2])
    return answer
