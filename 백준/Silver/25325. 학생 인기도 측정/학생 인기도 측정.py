import sys
input=sys.stdin.readline

n=int(input())
# print(n)
dic=dict()
for k in list(input().split()):
    dic[k]=0
# print(dic)
A=list(list(input().split())for _ in range(n))
for a in A:
    for i in range(len(a)):
        dic[a[i]]+=1

for k,v in sorted(list(dic.items()),key=lambda x: -x[1]):
    print(k,v)
