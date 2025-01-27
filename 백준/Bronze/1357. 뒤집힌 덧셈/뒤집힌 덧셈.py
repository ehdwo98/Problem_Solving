import sys
input=sys.stdin.readline

x,y=map(int,input().split())
def rev(n):
    res=int(''.join(str(n)[::-1]))
    return res

print(rev(rev(x)+rev(y)))