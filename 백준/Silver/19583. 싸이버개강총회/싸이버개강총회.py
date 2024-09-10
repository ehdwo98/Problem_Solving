import sys
input=sys.stdin.readline

s,e,q=input().split()
s=tuple(map(int,s.split(':')))
e=tuple(map(int,e.split(':')))
q=tuple(map(int,q.split(':')))

#print(s,e,q)

dic=dict()
while 1:
   try:
      a,b=input().split()
      a=tuple(map(int,a.split(':')))
      if b not in dic:
         dic[b]=list()
      dic[b].append(a)
   except:
      break

#print(dic)

ans=0
for key,values in dic.items():
   c1,c2=0,0
   for value in values:
      if value<=s:
         c1=1
      if e<=value<=q:
         c2=1
   if c1&c2:
      ans+=1

print(ans)