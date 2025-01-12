import sys
input=sys.stdin.readline

arr=list(input().rstrip())

for a in arr:
    if a.isalpha()==1:
        if a.isupper()==1:
            res=(ord(a)+13-ord('A'))%26+ord('A')
        else:
            res=(ord(a)+13-ord('a'))%26+ord('a')
        print(chr(res),end='')
    else:
        print(a,end='')