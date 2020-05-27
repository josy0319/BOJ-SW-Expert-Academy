def solution(weight):
    res = 1
    w = sorted(weight)
    for i in w:
        if res<i:
            break
        res+=i
    return res

