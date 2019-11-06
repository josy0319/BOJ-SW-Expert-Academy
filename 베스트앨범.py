# programmers 베스트앨범
# data = sorted(data, lambda x : x( ))이 가능 --> ()안에 ,로 여러개 조건 줄 수 있고 -쓰면 역순 정렬

def solution(genres, plays):
    answer = []
    num = []
    a = []
    count = 1
    for i in range(0,len(genres)):
        num.append(i)
    d = list(zip(genres, plays,num))
    d.sort(reverse=True)
    sum = d[0][1]
    for i in range(0,len(genres)-1):
        if(d[i][0] == d[i+1][0]):
            sum = sum + d[i+1][1]
            count+=1
        else :
            for j in range(0,count):
                a.append(sum)
            sum = d[i+1][1]
            count = 1
    for k in range(0,count):
                a.append(sum)
    d = list(zip(a,d))
    d = sorted(d, key = lambda x : (x[0],x[1][1],-x[1][2]), reverse=True)
    score = 1
    answer.append(d[0][1][2])
    for l in range(0,len(d)-1):
        if d[l][0] != d[l+1][0]:
            answer.append(d[l+1][1][2])
            score=1
        elif d[l][0] == d[l+1][0] and score < 2:
            answer.append(d[l+1][1][2])
            score += 1
    return answer
