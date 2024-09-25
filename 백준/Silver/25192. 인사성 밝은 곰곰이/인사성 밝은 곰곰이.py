import sys
input=sys.stdin.readline

n=int(input())

ans=0
dic=dict()
for i in range(n):
   tmp=input().rstrip()
   if tmp=='ENTER':
      ans+=len(dic.keys())
      dic=dict()
      continue
   dic[tmp]=1

ans+=len(dic.keys())
print(ans)