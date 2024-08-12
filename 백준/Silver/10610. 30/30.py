n=list(map(int,input().rstrip()))
#print(n)
if 0 in n and sum(n)%3==0:
   ans=sorted(n,reverse=True)
   print(int(''.join(map(str,ans))))
else:
   print(-1)