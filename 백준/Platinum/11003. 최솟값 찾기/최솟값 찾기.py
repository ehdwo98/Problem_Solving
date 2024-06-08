from collections import deque
import sys
input=sys.stdin.readline
n,l=map(int,input().split())
arr=list(map(int,input().split()))

stack=deque()
for i in range(n):
    while stack and stack[-1][1]>arr[i]:
        stack.pop()
    stack.append([i,arr[i]])
    while stack and (i-stack[0][0])>(l-1):
        stack.popleft()
    print(stack[0][1],end=' ')