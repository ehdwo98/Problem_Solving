import sys
input=sys.stdin.readline

n=int(input())

dic=dict()
for i in range(n):
   tmp=input().rstrip()
   dic[tmp]=i

dic2=dict()
for i in range(n):
   tmp=input().rstrip()
   dic2[tmp]=i

ans=0
out_keys=list(dic2.keys())
for i in range(len(dic2.keys())-1):
   now_in=dic[out_keys[i]]
   for j in range(i+1,len(out_keys)):
      next_in=dic[out_keys[j]]
      if next_in < now_in:
         ans+=1
         break
print(ans)