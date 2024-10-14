from itertools import permutations

n=int(input())
arr=list(map(int,input().split()))

P=permutations(arr,n)

ans=[]
for p in P:
   res=0
   for i in range(n-1):
      tmp=p[i]-p[i+1]
      if tmp<0:
         res+=(-tmp)
      else:
         res+=tmp
   ans.append(res)

print(sorted(ans)[-1])