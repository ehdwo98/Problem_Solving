from collections import Counter

a=int(input())
b=int(input())
c=int(input())

arr=list(map(int,''.join(str(a*b*c))))
i=list(Counter(arr).items())
#print(i)

ans=[0]*10

for p in i:
    k,v=p
    ans[k]=v

for a in ans:
    print(a)