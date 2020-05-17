#Programmer - n진수 게임

'''
진법 변환하는 재귀함수
응용 잘 할 수 있도록 반복 연습하기
진법은 곧 몫과 나머지
'''


def div(num, n):
    case = '0123456789ABCDEF'
    x,y = divmod(num,n)
    if x == 0:
        return case[y]
    else:
        return div(x,n) + case[y]
def solution(n,t,m,p):
    temp = ''
    res = ''
    num = 0
    while len(temp) < t*m:
        temp += div(num, n)
        num += 1
    res = ''
    for i in range(p-1,t*m,m):
        res+=temp[i]
    return res
