import sys
input=sys.stdin.readline
arr=list(input().rstrip())
print("1") if arr==arr[::-1] else print("0")