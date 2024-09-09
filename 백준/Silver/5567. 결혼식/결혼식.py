import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

dic=dict()
dic[1]=[]

for _ in range(m):
   a,b=map(int,input().split())
   if a not in dic:
      dic[a]=list()
   if b not in dic:
      dic[b]=list()
   dic[a].append(b)
   dic[b].append(a)

ans=[]
for i in dic[1]:
   ans.append(i)
   if i in dic:
      for j in dic[i]:
         ans.append(j)

ans=set(ans)

if len(ans)>0:
   print(len(ans)-1)
else:
   print(0)