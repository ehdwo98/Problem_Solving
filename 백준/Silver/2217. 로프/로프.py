n=int(input())

arr=list(int(input()) for _ in range(n))

arr.sort(reverse=True)
ans=0
for i in range(n):
    ans=max(ans,arr[i]*(i+1))

print(ans)