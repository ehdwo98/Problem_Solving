from collections import Counter
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

if set(res2)>set(res1):
   res1,res2=res2,res1

count=Counter(res2)

ans=0
for n in res1:
   ans+=count[T-n]

print(ans)