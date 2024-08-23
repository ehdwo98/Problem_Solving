from collections import Counter

T=int(input())
for _ in range(T):
   n=int(input())
   arr=tuple(input().rstrip().split()[1] for _ in range(n))
   #print(arr)
   C=list(Counter(arr).items())
   #print(C)
   ans=1
   for c in C:
      k,v=c
      ans*=(v+1)
   ans-=1
   print(ans)