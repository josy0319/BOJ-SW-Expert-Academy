#Progammers - H-index

def solution(c):
    if sum(c) == 0:
        return 0
    c = sorted(c,reverse=True)
    print(c)
    for i in range(len(c)-1):
        if i+1 >= c[i+1]:
            return i+1
    return len(c)
