n=int(input())
arr=list(map(int,input().split()))

ans=float("INF")
l=0
r=0
for i in range(n-1):
   s=i+1
   e=n-1
   cur=arr[i]
   while s<=e:
      mid=(s+e)//2
      res=cur+arr[mid]
      if abs(res)<ans:
         ans=abs(res)
         l=i
         r=mid
         if res==0:
            break
      if res<0:
         s=mid+1
      else:
         e=mid-1

print(arr[l],arr[r])