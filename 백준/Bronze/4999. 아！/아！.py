import sys
input=sys.stdin.readline

arr1=input().rstrip()
arr2=input().rstrip()

if arr2 in arr1:
    print('go')
else:
    print('no')