#BOJ - 파도반 수열

'''
점화식
'''


for i in range(int(input())):
    n = int(input())
    res = [0]*(n+5)
    res[0], res[1], res[2], res[3], res[4] = 1,1,1,2,2
    if n > 4:
        for i in range(5,n+1):
            res[i] = res[i-5]+res[i-1]
    print(res[n-1])
