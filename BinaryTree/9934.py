#BOJ - 완전 이진 트리


import math

k = int(input())
n = list(map(int,input().split()))
n.insert(0,0)
tree = [[] for _ in range(k+1)]
k_list = list(range((k+1)))
k_list = [2**i for i in k_list]

for i in range(1,(2**k)):
    for j in k_list:
        if i//j&1==1:
            tree[int(math.log2(j)+1)].append(n[i])
            break

for i in range(k,0,-1):
    for j in tree[i]:
        print(j, end=' ')
    print()
