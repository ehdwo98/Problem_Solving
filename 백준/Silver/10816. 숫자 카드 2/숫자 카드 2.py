from collections import Counter

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr=Counter(arr)

arr2=list(map(int,input().split()))
for a in arr2:
    print(arr[a],end=' ')