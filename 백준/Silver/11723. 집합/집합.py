import sys
input=sys.stdin.readline

M=int(input())

S=set()
for _ in range(M):
    p=input().split()
    if len(p)>1:
        a,b=p
        b=int(b)
    else:
        a=p[0]
    if a=='add':
        S.add(b)
    elif a=='remove':
        try:
            S.remove(b)
        except:
            pass
    elif a=='check':
        if b in S:
            print(1)
        else:
            print(0)
    elif a=='toggle':
        if b in S:
            S.remove(b)
        else:
            S.add(b)
    elif a=='all':
        S=set(i for i in range(1,21))
    else:
        S=set()