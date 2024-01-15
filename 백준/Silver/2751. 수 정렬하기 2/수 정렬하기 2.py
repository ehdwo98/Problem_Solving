from sys import stdin
input=stdin.readline

n=int(input())
arr=list()
for _ in range(n):
    tmp=int(input())
    arr.append(tmp)

arr=sorted(arr)

for a in arr:
    print(a)