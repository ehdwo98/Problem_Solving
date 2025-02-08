import sys
input=sys.stdin.readline

n=int(input())
arr=sorted(list(int(input())for _ in range(n)))
# print(arr)
if n<3:
    print(sum(arr))
else:
    tmp=0
    m,s=divmod(n,3)
    for i in range(m):
        tmp+=arr[s+3*i]
    print(sum(arr)-tmp)