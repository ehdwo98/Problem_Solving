n,m=map(int,input().split())

dic=dict(input().split() for _ in range(n))

arr=list(input().rstrip() for _ in range(m))

for a in arr:
   print(dic[a])