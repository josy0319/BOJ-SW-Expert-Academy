# BOJ - 집합의 표현

'''
disjoint-set -> Union-Find 자료구조
원소가 같은 루트값을 가지는지 효과적으로 체크해주는 구조

'''


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x] 

def union(a, b):
    root1 = find(a)
    root2 = find(b)
    if root1 != root2:
        if root1 > root2:
            parent[root2] = root1
        else:
            parent[root1] = root2

n, m= map(int, input().split())
parent= [i for i in range(n+1)]

for i in range(m):
    bit, a, b= map(int, input().split())
    if bit:
        if find(a)== find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)

