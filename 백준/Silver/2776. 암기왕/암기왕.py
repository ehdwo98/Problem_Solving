import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
   n=int(input())
   arr=list(map(int,input().split()))
   dic=dict()
   for a in arr:
      dic[a]=1

   m=int(input())
   arr2=list(map(int,input().split()))
   for a in arr2:
      if a not in dic:
         print(0)
      else:
         print(1)