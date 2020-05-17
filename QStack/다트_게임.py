#Programmers - 다트 게임

'''
처리하기 까다롭다고 생각되는 문자열이 있을때(이 문제에서는 10),
replace로 치환하여 처리하면 훨씬 간결하게 처리할 수 있음

여러개의 종류를 목록별로 확인해야 할 때,
그 목록들을 리스트로 만들어 in을 사용하면 더욱 간결
'''


def solution(d):
    res = []
    num = []
    char = []
    i = 0
    while i < len(d):
        if d[i].isdecimal() and d[i+1].isdecimal():
            num.append(int(d[i]+d[i+1]))
            i+=2
        elif d[i].isdecimal():
            num.append(int(d[i]))
            i+=1
        elif d[i].isalpha():
            char.append(d[i])
            if len(d) > i+1 and d[i+1].isdecimal() == False:
                char.append(d[i+1])
                i+=1
            i+=1
    while char:
        if char[0] == '*':
            res[-1] *= 2
            if len(res) > 1:
                res[-2] *= 2
        elif char[0] == '#':
            res[-1] *= -1
        c_temp = char.pop(0)
        if c_temp == 'S':
            res.append(num.pop(0) ** 1)
        elif c_temp == 'D':
            res.append(num.pop(0) ** 2)
        elif c_temp == 'T':
            res.append(num.pop(0) ** 3)
    return sum(res)
    
    
    
    
