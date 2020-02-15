#Programmers - 영어 끝말잇기



def solution(n, words):
    temp = []
    cnt = 0
    res = 0
    l = len(words)
    while words:
        cnt += 1
        x = words.pop(0)
        if x in temp:
            res = cnt
            cnt = ((cnt-1)%n)+1
            break
        elif temp and x[0] != temp[-1][-1]:
            res = cnt
            cnt = ((cnt-1)%n)+1
            break
        else:
            temp.append(x)
    if res and res%n == 0:
        res= res//n
    elif res and res%n != 0:
        res= (res//n)+1
    return [cnt,res] if cnt != l else [0,0]


