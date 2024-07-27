n,k=map(int,input().split())

arr=list(int(input()) for _ in range(n))

ans=0
while k:
    p=arr.pop()
    cnt,k=divmod(k,p)
    ans+=cnt

print(ans)