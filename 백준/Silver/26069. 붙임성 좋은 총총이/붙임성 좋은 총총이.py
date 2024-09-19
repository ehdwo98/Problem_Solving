n=int(input())

dic=dict()
for _ in range(n):
   a,b=input().rstrip().split()
   if a=='ChongChong' or b=='ChongChong':
      dic[a]=1
      dic[b]=1
   if a in dic:
      dic[b]=1
   if b in dic:
      dic[a]=1

print(len(dic.keys()))