import sys
input=sys.stdin.readline
arr=list(input().rstrip())
for i in range(len(arr)):
    if i%10==0 and i!=0:
        print()
    print(arr[i],end='')