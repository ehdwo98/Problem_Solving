import sys
input=sys.stdin.readline

n=int(input())

arr=list(sorted(list(map(int,input().split()))[1::]) for _ in range(n))
arr2=list(sorted(list(a[i]-a[i-1] for i in range(1,len(a)))) for a in arr)

for i in range(n):
    print(f"Class {i+1}")
    print(f"Max {arr[i][-1]}, Min {arr[i][0]}, Largest gap {arr2[i][-1]}")
