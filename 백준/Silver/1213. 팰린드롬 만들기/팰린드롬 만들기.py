import sys
input=sys.stdin.readline
from collections import Counter

arr=list(input().rstrip())
counter=list(Counter(arr).items())

cnt=0
res=''
for k,v in counter:
    if v%2==1:
        cnt+=1
        res=k
    if cnt>1:
        print("I'm Sorry Hansoo")
        exit(0)

tmp=''
for k,v in sorted(counter):
    tmp+=k*(v//2)
print(tmp+res+tmp[::-1])