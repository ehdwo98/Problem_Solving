import sys
input=sys.stdin.readline

a,b=map(int,input().split())

arr=set(map(int,input().split()))
brr=set(map(int,input().split()))

ab=list(arr-brr)
ba=list(brr-arr)

# print(ab,ba)
print(len(ab)+len(ba))