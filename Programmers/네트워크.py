#Programmers - 네트워크

'''
union-find
'''


def find(num):
    global l
    if l[num] != num:
        l[num] = find(l[num])
    return l[num]
def union(a, b):
    global l, res
    aa = find(a)
    bb = find(b)
    l[aa] = bb
def solution(n, computers):
    global l, res
    res = 0
    l = list(range(n+1))
    
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                union(i+1,j+1)
    for idx, i in enumerate(l[1:]):
        if i==idx+1:
            res+=1
    return res
