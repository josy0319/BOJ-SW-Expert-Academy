#BOJ - 가운데를 말해요

'''
속도를 줄이기 위한 노력
->입력을 sys.stdin.readline()으로 받기.
  sort()는 시간복잡도가 nlogn이므로 대신 insert()를 사용하여
  시간복잡도를 줄임. insert()의 시간복잡도는 n이다.
  python보다는 pypy3
'''


import sys
import bisect as bs

n = int(sys.stdin.readline())
num = []
for i in range(n):
    a = int(sys.stdin.readline())
    if len(num) == 0:
        num.append(a)
    else:
        num.insert(bs.bisect(num,a),a)
    
    if (i//2)&1!=1 and len(num)&1!=1:
        if num[i//2] > num[i//2+1]:
            print(num[i//2+1])
        else:
            print(num[i//2])
    else:
        print(num[i//2])
