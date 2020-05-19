#Programmers - 가장 긴 팰린드롬

'''
단순 구현
'''

def solution(s):
    res = 0
    for i in range(0,len(s)):
        for j in range(1,len(s)+1-i):
            normal = s[i:i+j]
            reverse = normal[::-1]
            if normal == reverse and j > res:
                res = j
    return res
