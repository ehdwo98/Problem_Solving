n,m=map(int,input().split())

group=dict()
for _ in range(n):
   team=input().rstrip()
   num=int(input())
   members=sorted(list(input().rstrip() for _ in range(num)))
   group[team]=members

#print(group)

arr=[]
for _ in range(m):
   name=input().rstrip()
   cmd=int(input())
   arr.append([name,cmd])

#print(arr)

for a in arr:
   name,cmd=a
   if cmd==1:
      for k,v in group.items():
         if name in v:
            print(k)
   else:
      for mem in group[name]:
         print(mem)