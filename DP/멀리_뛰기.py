#Programmers - 멀리 뛰기

'''
DP 기초
'''

def solution(n):
    res = 0
    temp = [1, 2, 3, 5]
    for i in range(4, n):
        temp.append(temp[i-1]+temp[i-2])
    return temp[n-1]%1234567
