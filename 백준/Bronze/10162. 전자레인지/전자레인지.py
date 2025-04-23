import sys
input=sys.stdin.readline

T=int(input())

a,res=divmod(T,300)
b,res=divmod(res,60)
c,res=divmod(res,10)
if res!=0:
    print(-1)
else:
    print(a,b,c)