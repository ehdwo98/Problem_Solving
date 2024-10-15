from itertools import permutations

n=int(input())
arr=list(i for i in range(1,n+1))

P=permutations(arr,n)

for p in P:
   print(*p)