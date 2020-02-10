#Programmers - 다음 큰 숫자

'''
bin() -> 2진수 변환 (oct,hex 등)
int(a,b) -> b진수의 값 a를 10진수로 변환
'''

def solution(n):
    n_bin = bin(n).replace('0b','')
    res = n+1
    while True:
        res_bin = bin(res).replace('0b','')
        if n < res and n_bin.count('1') == res_bin.count('1') :
            break
        res +=1 
    return res
