e,s,m=map(int,input().split())
e=e%15
s=s%28
m=m%19

i=1
while 1:
   if i%15==e and i%28==s and i%19==m:
      print(i)
      break
   i+=1