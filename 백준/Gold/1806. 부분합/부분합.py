n,s=map(int,input().split())

arr=list(map(int,input().split()))

start,end=0,0
res=[]
ans=float('inf')
sum=0
while start<=end:
   if sum>=s:
      ans=min(ans,end-start)
      sum-=arr[start]
      start+=1
   elif end==n:
      break
   else:
      sum+=arr[end]
      end+=1

if ans==float('inf'):
   print(0)
else:
   print(ans)