import sys
input=sys.stdin.readline

n=int(input())

f=[0]*100

f[0]=0
f[1]=1
if n<2:
    print(n)
else:
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    print(f[n])