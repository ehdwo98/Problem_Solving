from collections import defaultdict
import sys
input=sys.stdin.readline

n=int(input())

dic=defaultdict(int)
cnt=0

for _ in range(n):
    tmp=list(input().rstrip())
    c=1
    for i in range(len(tmp)):
        if ''.join(tmp) in dic:
            c=0
            break
        p=tmp.pop(0)
        tmp.append(p)
    if c:
        dic[''.join(tmp)]+=1
        cnt+=1

print(cnt)