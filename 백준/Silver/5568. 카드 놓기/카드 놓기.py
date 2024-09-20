from itertools import permutations

n=int(input())
k=int(input())

arr=list(input() for _ in range(n))

parr=permutations(arr,k)

dic=dict()
for p in parr:
   tmp=''.join(list(p))
   if tmp not in dic:
      dic[tmp]=1

print(len(dic.keys()))