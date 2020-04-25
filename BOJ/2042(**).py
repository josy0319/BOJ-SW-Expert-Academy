#BOJ - 구간 합 구하기4

'''
세그먼트 트리
'''

import sys

input = sys.stdin.readline

#세그먼트 트리와 dp가 핵심이 될 것

#1, 0, n-1
def init(node, start, end):
    #node가 leaf 노드인 경우 배열의 원소 값을 반환.
    if start==end:
        tree[node]=l[start]
        return tree[node]
    else:
        #재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합 저장
        tree[node]=init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    #diff가 양수건 음수건 현 node에 더해줘야 함.
    tree[node] += diff

    #리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에 검사
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return subSum(node*2, start, (start+end)//2, left, right) + \
        subSum(node*2+1, (start+end)//2+1, end, left, right)

#수집합의 갯수/변경이 일어나는 수/구간합을 구하는 수
n, m, k = map(int, input().split())
l = []
tree = [0] * 3000000
for _ in range(n):
    l.append(int(input()))

#1=변경, 2=합

init(1, 0, n-1)
print(tree[:20])

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a==1:
        b-=1
        diff=c-l[b]
        l[b]=c
        update(1, 0, n-1, b, diff)
    elif a==2:
        print(subSum(1, 0, n-1, b-1, c-1))
