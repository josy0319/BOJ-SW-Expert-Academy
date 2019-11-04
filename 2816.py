// 2816.디지털 티비(BOJ)

def a(x) :
    score = []
    i = 0
    j = 0
    i = x.index('KBS1')
    for k in range(i):
        score.append("1")
    for k in range(i):    
        score.append("4")

    j = x.index('KBS2')
    if i>j :
        for k in range(j+1):
            score.append("1")
        for k in range(j):
            score.append("4")  
    else :
        j = x.index('KBS2')
        for k in range(j):
            score.append("1")
        for k in range(j-1):
            score.append("4")

    return score

if __name__ =="__main__":
    x = []
    num = int(input().strip())
    for i in range(num):
       x.append(input().strip())
    print("".join(a(x)))
