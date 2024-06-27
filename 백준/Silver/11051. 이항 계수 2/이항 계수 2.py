n,k=map(int,input().split())

a=1
for i in range(n-k+1,n+1):
    a*=i
b=1
for i in range(1,k+1):
    b*=i

ans=(a//b)%10007
print(ans)