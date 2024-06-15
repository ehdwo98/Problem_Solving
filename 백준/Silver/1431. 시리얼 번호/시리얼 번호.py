import sys
input=sys.stdin.readline

arr=[]
n=int(input())

for _ in range(n):
    ip=input().strip()
    arr.append(ip)

arr.sort(key=lambda x:(len(x),sum([int(n) for n in x if n.isdigit()]),x))
for a in arr:
    print(a)