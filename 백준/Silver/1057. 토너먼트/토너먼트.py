import math
n,a,b=map(int,input().split())

cnt=0
while a!=b:
   a=math.ceil(a/2)
   b=math.ceil(b/2)
   cnt+=1

print(cnt)