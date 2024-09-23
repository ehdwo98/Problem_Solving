import sys
input=sys.stdin.readline

n,m=map(int,input().split())

dic=dict()
for i in range(n):
   tmp=input().rstrip()
   if len(tmp)>=m:
      if tmp not in dic:
         dic[tmp]=1
      else:
         dic[tmp]+=1

res=sorted(list(dic.items()),key=lambda x:(-x[1],-len(x[0]),x[0]))

for k,v in res:
   print(k)