n,m=map(int,input().split())

arr=list(int(input()) for _ in range(n))
arr.sort()

ans=float('inf')
s,e=0,0

while e<n:
   res=arr[e]-arr[s]
   if res>=m:
      s+=1
      ans=min(ans,res)
      if ans==m:
         break
   else:
      e+=1

print(ans)