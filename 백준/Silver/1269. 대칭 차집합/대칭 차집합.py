import sys
input=sys.stdin.readline

a,b=map(int,input().split())

arr=set(map(int,input().split()))
arr^=set(map(int,input().split()))

print(len(arr))