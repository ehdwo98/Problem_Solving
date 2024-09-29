import bisect
import sys
input=sys.stdin.readline

T=int(input())

n=int(input())
arr=list(map(int,input().split()))
res1=list()
for i in range(len(arr)):
   tmp=0
   for j in range(i,len(arr)):
      tmp+=arr[j]
      res1.append(tmp)

m=int(input())
arr=list(map(int,input().split()))
res2=list()
for i in range(len(arr)):
   tmp=0
   for j in range(i,len(arr)):
      tmp+=arr[j]
      res2.append(tmp)

res1.sort()
res2.sort()

ans=0
for i in range(len(res1)):
   l=bisect.bisect_left(res2,T-res1[i])
   r=bisect.bisect_right(res2,T-res1[i])
   ans+=(r-l)

print(ans)