#BOJ - 보물



n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
res=0
a = sorted(a,reverse=True)
b = sorted(b,reverse=False)
for i in range(len(a)):
    res+=a[i]*b[i]
print(res)
