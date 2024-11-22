import sys
input=sys.stdin.readline

w,h,x,y,p=map(int,input().split())

ans=0
for _ in range(p):
    a,b=map(int,input().split())
    c=0
    if x<=a<=x+w and y<=b<=y+h:
        c=1
    elif a<x:
        if (a-x)*(a-x)+(y+h//2-b)*(y+h//2-b)<=(h//2)*(h//2):
            c=1
    elif a>x+w:
        if (a-x-w)*(a-x-w)+(y+h//2-b)*(y+h//2-b)<=(h//2)*(h//2):
            c=1
    else:
        c=0
    if c:
        ans+=1
print(ans)