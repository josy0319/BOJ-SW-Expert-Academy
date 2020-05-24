#Programmers - 행렬의 곱셈

'''
단순 구현
numpy
'''


import numpy as np
def solution(arr1, arr2):
    res = []
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    for i in list(arr1@arr2):
        res.append(list(i))
    return res
