#Programmers - 땅따먹기

'''
효율성문제에는 DFS 지양하기
'''


def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][1],land[i][0],land[i][3])
        land[i+1][3] += max(land[i][1],land[i][2],land[i][0])
    return max(land[len(land)-1])
    
    
#--------------------------------------------------------
    
    
import sys 
sys.setrecursionlimit(10**6)

def DFS(L,m,land):
    global a
    global temp
    if L == len(land):
        if a < sum(temp):
            a = sum(temp)
    else:
        for i in range(0,4):
            if m != i :
                temp[L] = land[L][i]
                DFS(L+1,i,land)
                
def solution(land):
    global temp
    global a
    temp = [0]*len(land)
    a = 0
    DFS(0,0,land)
    return a
