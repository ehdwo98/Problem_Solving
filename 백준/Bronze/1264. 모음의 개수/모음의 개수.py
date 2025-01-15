import sys
input=sys.stdin.readline

while True:
    arr=input().rstrip().lower()
    if arr=='#':
        break
    cnt=0
    for a in ['a','e','i','o','u']:
        cnt+=arr.count(a)
    print(cnt)
