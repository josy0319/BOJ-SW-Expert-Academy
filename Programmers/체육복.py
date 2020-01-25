#Programmers - 체육복

def solution(n, lost, reserve):
    student = list(range(1,n+1))
    temp = list(range(1,n+1))
    for i in temp:
        if i in lost:
            if i in reserve:
                lost.remove(i)
                reserve.remove(i)
        if i in lost :
            student.remove(i)
    for item in reserve:
        if item not in student:
            student.append(item)
        elif item-1 not in student and item-1 > 0:
            student.append(item-1)
        elif item+1 not in student and item+1 <= n:
            student.append(item+1)
    return len(student)
