#BOJ - 리모콘

'''
완전탐색(브루트포스)
'''


def dfs(a):
    if len(a) == len(str(n))+1 :
        if a != '':
            temp_list.append(int(a))
    else:
        for i in button:
            a += str(i)
            dfs(a)
            if len(a) == len(str(n)):
                temp_list.append(int(a))
            elif len(a)-1 > 0 and len(a) == len(str(n))-1:
                temp_list.append(int(a))
            a = a[:-1]       

n = int(input())
m = int(input())
if m != 0:
    e = list(map(int, input().split()))
else:
    e = []
button = list(range(10))
for i in e:
    if i in button:
        button.pop(button.index(i))

temp = ''
temp_list = []
temp_list += button
dfs(temp)

res = 2147000000
digit = 2147000000
for i in temp_list:
    if abs(i-n) <= res:
        if res + digit < abs(i-n) + len(str(i)):
            continue
        res = abs(i-n)
        digit = len(str(i))

result = digit+res
if abs(n-100) < result:
    result = abs(n-100)

print(result)
        
