#Programmers - 비밀지도

def solution(n, arr1, arr2):
    answer = []
    a,b = [], []
    for i in arr1:
        temp = str(bin(i).replace('0b',''))
        if len(temp) == n:
            a.append(temp)
        else:
            a.append('0'*(n-len(temp))+temp)
    for i in arr2:
        temp = str(bin(i).replace('0b',''))
        if len(temp) == n:
            b.append(temp)
        else:
            b.append('0'*(n-len(temp))+temp)
    res = [[0]*len(a) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if int(a[i][j]) | int(b[i][j]) == 1:
                res[i][j] = '#'
            else:
                res[i][j] = ' '
    answer = []
    for i in res:
        answer.append(''.join(i))
    return answer
