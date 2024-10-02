n=int(input())

for _ in range(n):
   tmp=input().rstrip()
   cnt=0
   res=0
   for t in tmp:
      if t=='O':
         cnt+=1
         res+=cnt
      else:
         cnt=0
   print(res)