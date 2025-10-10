import sys
input=sys.stdin.readline

n=int(input())

arr=list(input().rstrip() for _ in range(n))

arr2=sorted(arr)
if arr==arr2:
    print("INCREASING")
elif arr==arr2[::-1]:
    print("DECREASING")
else:
    print("NEITHER")