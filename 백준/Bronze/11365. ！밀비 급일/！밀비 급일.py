import sys
input=sys.stdin.readline

while 1:
    res=input().rstrip()
    if res=='END':
        break
    print(res[::-1])
