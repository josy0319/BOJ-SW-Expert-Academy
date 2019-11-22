#Programmers - 위장

def solution(clothes):
    answer = 0
    list = []
    count = 1
    temp = ''
    sum = 1
    for i in range(0,len(clothes)):
        temp = clothes[i][1]
        clothes[i][1] = clothes[i][0]
        clothes[i][0] = temp
    clothes.sort()
    for i in range(0,len(clothes)-1):
        if(clothes[i][0] != clothes[i+1][0]):
            list.append(count)
            count = 1
        else : count+=1
    list.append(count)
    for i in range(0,len(list)):
        sum = sum * (list[i]+1)
    answer = sum -1
    return answer
