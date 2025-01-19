import sys
input=sys.stdin.readline

res=input().rstrip()
if res!='F':
    a,b=res
else:
    print(0.0)
    exit()
ans=0
if a=='A':
    ans+=4
elif a=='B':
    ans+=3
elif a=='C':
    ans+=2
elif a=='D':
    ans+=1
else:
    ans+=0.0
if b=='+':
    ans+=0.3
elif b=='0':
    ans+=0.0
else:
    ans-=0.3

print(ans)