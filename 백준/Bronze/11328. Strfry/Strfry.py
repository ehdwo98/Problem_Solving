import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    a,b=input().split()
    a=list(a.strip())
    b=list(b.strip())
    cnt=0
    i=0
    while i<len(a):
        if a[i] in b:
           b.remove(a[i])
           a.remove(a[i])
           i-=1
        i+=1
    if len(a)==0 and len(b)==0:
        print("Possible")
    else:
        print("Impossible")