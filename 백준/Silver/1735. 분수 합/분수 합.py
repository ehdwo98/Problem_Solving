import math
arr=list(list(map(int,input().split())) for _ in range(2))
# print(arr)
b=math.lcm(arr[0][1],arr[1][1])
a=int(arr[0][0]*(b/arr[0][1]))+int(arr[1][0]*(b/arr[1][1]))

g=math.gcd(a,b)
if g==1:
   print(a,b)
else:
   print(a//g,b//g)