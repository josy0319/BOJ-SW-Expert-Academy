#Programmers - 피보나치 수

'''
동적 프로그래밍(Top-Down)
점화식(Bottom-Up)
'''

def solution(n):
    arr = [0]*(n+1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]%1234567

#-----------------------------------

import sys
sys.setrecursionlimit(10**6)

def DFS(x):
    global arr
    if arr[x] > 0:
        return arr[x]
    if x == 0 or x == 1:
        return x
    else:
        arr[x] = DFS(x-1) + DFS(x-2)
        return arr[x]
def solution(n):
    global arr
    arr = [0]*(n+1)
    return DFS(n)%1234567
