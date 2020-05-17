#Programmers - 타켓 넘버

'''
DFS 기초문제
'''

def solution(n,a):
    global cnt
    cnt = 0
    DFS(0,0,n,a)
    return cnt
def DFS(L,sum,numbers,a):
    global cnt
    if L == len(numbers):
        if sum == a:
            print(sum)
            cnt+=1
    else:
        DFS(L+1,sum+numbers[L],numbers,a)
        DFS(L+1,sum-numbers[L],numbers,a)
