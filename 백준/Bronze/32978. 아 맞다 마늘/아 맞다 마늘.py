import sys
input=sys.stdin.readline

n=int(input())
# print(n)
dic=dict()
for k in list(input().split()):
    dic[k]=1
for k in list(input().split()):
    dic[k]-=1
for k,v in dic.items():
    if v==1: print(k)