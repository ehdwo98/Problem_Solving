import sys
input=sys.stdin.readline

n,d=map(int,input().split())

arr=list(x for x in range(1,n+1))
arr2=''.join(map(str,arr))
# print(arr2)
print(arr2.count(str(d)))