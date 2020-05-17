#Programmers - 2016년

'''
# day[(sum(month[:a-1])+b-1)%7]
리스트의 값들을 순차적으로 더해야 하는 경우,
for로 순회하기 보다는 슬라이스와 sum으로 더 효율적으로 작성 가능
'''

def solution(a, b):
    date = b
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = day[(date-1) % 7]
    for i in range(a-1):
        date = date + month[i]
        answer = day[(date-1) % 7]
    return answer
