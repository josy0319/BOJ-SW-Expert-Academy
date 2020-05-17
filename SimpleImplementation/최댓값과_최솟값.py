#Programmers - 최댓값과 최솟값
'''
split 공백으로 자르기
'''


def solution(s):
    temp = [0] * (len(s)//2+1)
    st = ''
    j = 0
    for idx,i in enumerate(s):
        if i != ' ':
            st += i
        else:
            temp[j] = st
            st = ''
            j+=1
        if idx+1 == len(s):
            temp[j] = st
    while j+1 != len(s)//2+1:
        temp.pop()
        j+=1
    max = -100000
    min = 100000
    for j in temp:
        if int(j) > max:
            max = int(j)
        if int(j) < min:
            min = int(j)
    return str(min)+' '+str(max)
   
   
#-------------------------------------------
   
   
def solution(s):
    temp = list(map(int,s.split()))
    return str(min(temp))+' '+str(max(temp))
