import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    arr=list(input().rstrip().split())
    for a in arr:
        print(a[::-1],end=' ')