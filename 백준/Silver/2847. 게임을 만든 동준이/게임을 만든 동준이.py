n=int(input())

arr=list(int(input()) for _ in range(n))
arr.reverse()

cnt=0
for i in range(n-1):
   if arr[i]<=arr[i+1]:
      while arr[i]<=arr[i+1]:
         arr[i+1]-=1
         cnt+=1

print(cnt)