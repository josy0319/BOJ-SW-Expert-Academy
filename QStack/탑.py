#programmers - 탑

def solution(heights):
    answer = []
    #4 7 5 9 6
    for i in range(len(heights)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                break    
            if j == 0:
                answer.append(0)
                break
    answer.append(0)
    answer.reverse()
    return answer
