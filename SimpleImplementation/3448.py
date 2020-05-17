#BOJ - 문자인식


import sys
for i in range(int(input())):
    b_s=''
    while True:
        b = sys.stdin.readline()
        if b != '\n':
            b_s+=b[:-1]
        else:
            break
    b_l = len(b_s)
    a_s = b_s.replace("#",'')
    a_l = len(a_s)
    print("Efficiency ratio is %.1f" % round(a_l/b_l*100,1)+'%.') if round(a_l/b_l*100,1)-int(round(a_l/b_l*100,1))!=0 else print("Efficiency ratio is %d" % round(a_l/b_l*100,1)+'%.')
