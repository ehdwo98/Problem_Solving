import sys
input=sys.stdin.readline

def r(n):
   if n-int(n)>=0.5:
      return int(n)+1
   return int(n)

n=int(input())
if n==0:
   print(0)
else:
   w=r(n*0.15)
   arr=sorted(list(int(input()) for _ in range(n)))
   res=arr[w:n-w]
   print(r(sum(res)/(n-2*w)))