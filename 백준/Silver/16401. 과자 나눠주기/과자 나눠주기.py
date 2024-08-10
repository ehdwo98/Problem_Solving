import bisect
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)

s,e=1,int(1e9)
ans=0
while s<=e:
   mid=(s+e)//2
   cnt=0
   if mid==0:
      break
   for a in arr:
      if a>=mid:
         cnt+=(a//mid)
      else:
         break
   if cnt>=m:
      ans=max(ans,mid)
      s=mid+1
   else:
      e=mid-1

print(ans)