# 2309. 일곱 난쟁이

import sys

x = list()
resultArr = []
breaker = False
for i in range(0,9):
    x.append(int (sys.stdin.readline().rstrip('\n')))
for i in range(0,8) :
    for j in range(i+1,9) :
        temArr = x[:]
        del temArr[j]
        del temArr[i]
        if(sum(temArr)==100):
            resultArr = temArr
            breaker = True
    if breaker == True:
        break
resultArr.sort()
for k in range (0, 7):
    print(resultArr[k])
