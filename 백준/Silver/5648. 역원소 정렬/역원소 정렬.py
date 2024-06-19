import sys

input=sys.stdin.readline
arr=list(map(int,input().split()))

n=arr.pop(0)

while 1:
    if len(arr)==n:
        break
    arr.extend(list(map(int,input().split())))

#print(arr)

for i in range(n):
    arr[i]=int(str(arr[i])[::-1])

arr.sort()
for a in arr:
    print(a)