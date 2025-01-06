import sys
input=sys.stdin.readline

dic=dict()
n=int(input())
for _ in range(n):
    s,x=input().split()
    x=int(x)
    if s not in dic:
        dic[s]=x
    else:
        dic[s]+=x

for k,v in dic.items():
    if v==5:
        print("YES")
        exit(0)
print("NO")