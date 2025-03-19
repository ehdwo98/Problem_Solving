import sys
input=sys.stdin.readline

a,b=map(int,input().split())

def func(n,cnt):
    if n==b:
        print(cnt)
        exit(0)
    elif n<b:
        func(n*2,cnt+1)
        func(int(str(n)+'1'),cnt+1)
    else:
        return
func(a,1)
print(-1)