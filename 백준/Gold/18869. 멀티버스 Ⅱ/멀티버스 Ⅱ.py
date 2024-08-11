import bisect
from collections import Counter
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
ans=[]
for _ in range(m):
   arr=list(map(int,input().split()))
   arr2=sorted(arr)
   tmp=[]
   for a in arr:
      tmp.append(bisect.bisect_left(arr2,a))
   ans.append(tuple(tmp))
   
C=list(Counter(ans).items())
total=0
for c in C:
   v,cnt=c
   if cnt>1:
      for i in range(1,cnt):
         total+=i

print(total)