import sys
input=sys.stdin.readline

arr=input().rstrip()

for a in arr:
    if a.isupper()==1:
        print(a.lower(),end='')
    else:
        print(a.upper(),end='')