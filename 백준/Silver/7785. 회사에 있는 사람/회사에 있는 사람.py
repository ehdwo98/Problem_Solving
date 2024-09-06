n=int(input())

dic=dict(input().split() for _ in range(n))

ans=[]
for k,v in dic.items():
   if v=='enter':
      ans.append(k)

for a in sorted(ans,reverse=True):
   print(a)