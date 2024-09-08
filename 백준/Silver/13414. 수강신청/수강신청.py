import sys
input=sys.stdin.readline

K,L=map(int,input().split())

dic=dict()
for i in range(L):
   tmp=input().rstrip()
   if tmp in dic.keys():
      del dic[tmp]
      dic[tmp]=1
   else:
      dic[tmp]=1

#print(dic)
ans=list(dic.items())[:K]
for k,v in ans:
   print(k)