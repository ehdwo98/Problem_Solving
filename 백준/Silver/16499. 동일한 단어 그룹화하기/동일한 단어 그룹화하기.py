import sys
input=sys.stdin.readline

n=int(input())
arr=list(''.join(sorted(input().rstrip())) for _ in range(n))

dic=dict()
for a in arr:
    if a not in dic:
        dic[a]=1

print(len(dic))