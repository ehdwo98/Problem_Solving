import sys
input=sys.stdin.readline
n=int(input())

cnt,cnt1=0,0
while n>=3:
    if n%5==0:
        cnt+=1
        n-=5
    else:
        n-=3
        cnt1+=1

if n!=0:
    print(-1)
else:
    print(cnt+cnt1)