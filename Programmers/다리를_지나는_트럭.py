#Programmers - 다리를 지나는 트럭

'''
그림을 그려가며 문제 상황 표현하기
'''


def solution(bridge_length, weight, truck_weights):
    q = [0]*bridge_length
    sec = 0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec
