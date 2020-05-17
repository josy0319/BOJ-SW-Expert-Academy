#BOJ - 연속합

'''
다이나믹 프로그래밍
동적 계획법 
'''

#1차시기 - 일반적인 DP 시간 초과 -> O(N2)
n = int(input())
m = list(map(int, input().split()))

temp = [-1000 for i in range(n)]
temp[0] = m[0]
for i in range(n-1):
    res = m[i]
    for j in range(i+1,n):
        res += m[j]
        if temp[j] < res:
            temp[j] = res
print(max(temp))


#2차시기 - for루프로 1개 개선된 DP
n = int(input())
m = list(map(int, input().split()))

temp = [0 for i in range(n)]
temp[0] = m[0]
for i in range(1,n):
    temp[i] = max(temp[i-1]+m[i], m[i])
print(max(temp))
