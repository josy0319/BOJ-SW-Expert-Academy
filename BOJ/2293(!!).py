#BOJ - 동전1

'''
DP 점화식
'''


n, k = map(int,input().split())
coin=[int(input()) for _ in range(n)]
dp=[0 for i in range(k+1)]
dp[0]=1
for i in coin:
    for j in range(i,k+1):
        dp[j]+=dp[j-i]
print(dp[-1])

