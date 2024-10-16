from itertools import permutations

n=int(input())
cmd=list(input().split())
arr=list(i for i in range(10))

P=permutations(arr,n+1)

ans=[]
for p in P:
   c=1
   for i in range(len(cmd)):
      res=cmd[i]
      if res=='<':
         if p[i]>=p[i+1]:
            c=0
            break
      elif res=='>':
         if p[i]<=p[i+1]:
            c=0
            break
   if c:
      ans.append(''.join(map(str,p)))

# print(ans)
print(ans[-1])
print(ans[0])