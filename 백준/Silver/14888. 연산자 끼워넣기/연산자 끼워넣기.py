import sys
from itertools import permutations

input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr2=input().split()

seq=[]
for i in range(len(arr2)):
   if i==0:
      res='+'
   elif i==1:
      res='-'
   elif i==2:
      res='*'
   else:
      res='%'
   tmp=res*int(arr2[i])
   seq.extend(tmp)

P=permutations(seq,len(seq))

ans=[]
for p in P:
   res=arr[0]
   for i in range(1,len(arr)):
      if p[i-1]=='+':
         res+=arr[i]
      elif p[i-1]=='-':
         res-=arr[i]
      elif p[i-1]=='*':
         res*=arr[i]
      else:
         if res<0:
            res=-((-res)//arr[i])
         else:
            res//=arr[i]
   ans.append(res)

ans.sort()
print(ans[-1])
print(ans[0])