from collections import defaultdict
import sys
input=sys.stdin.readline

n=int(input())

dic=defaultdict(int)

for _ in range(n):
    dic[input().rstrip()]+=1

for _ in range(n-1):
    dic[input().rstrip()]-=1

for k,v in dic.items():
    if v!=0:
        print(k)