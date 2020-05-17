#Programmers - JadenCase 문자열 만들기

'''
title() / isnumeric() / isdigit() 등 문자열 함수
'''

def solution(s):
    s = s.title()
    for i in range(len(s)):
        if s[i].isnumeric() == True:
            s = s.replace(s[i+1],s[i+1].lower())
    return s
