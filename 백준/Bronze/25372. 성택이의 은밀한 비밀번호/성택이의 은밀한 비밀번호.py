import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    arr=input().rstrip()
    if 6<=len(arr)<=9:
        print('yes')
    else:
        print('no')
