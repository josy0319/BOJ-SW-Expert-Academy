#Programmers - 주식가격

'''
stack
'''


def solution(prices):
    length = len(prices)
    res = []
    for x in range(length):
        if x==length-1:
            res.append(0)
            break
        for y in range(x+1,length):
            if(prices[x]>prices[y]):
                res.append(y - x)
                break
            elif(y+1==length):
                res.append(length - (x+1))
            else:
                continue
    return res
