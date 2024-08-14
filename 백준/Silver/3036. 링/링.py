from math import gcd

n=int(input())
arr=list(map(int,input().split()))

cri=arr[0]
for i in range(1,n):
   g=gcd(cri,arr[i])
   a,b=cri//g,arr[i]//g
   if b==0:
      print(str(a)+'/'+str(1))
   else:
      print(str(a)+'/'+str(b))