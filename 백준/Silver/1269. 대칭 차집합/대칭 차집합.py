import sys
input=sys.stdin.readline

a,b=map(int,input().split())

arr=set(map(int,input().split()))
arr^=set(map(int,input().split()))
# print(set.difference(a,b), a-b) #차집합
# print(set.symmetric_difference(a,b), a^b) #대칭차집합

print(len(arr))