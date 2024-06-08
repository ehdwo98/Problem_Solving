from collections import deque
import sys
input=sys.stdin.readline
n,l=map(int,input().split())
arr=list(map(int,input().split()))
#인덱스접근은 list가 deque보다 빠르다. 
#list() -> 항상 O(1), deque() -> 처음과 끝은 O(1) 하지만, 가운데로 갈수록 O(n)
#deque가 이중 연결 리스트이기 때문
#인덱스접근만 할 경우, list()를 사용하는 것이 시간 효율이 좋다.
stack=deque()
for i in range(n):
    while stack and stack[-1][1]>arr[i]:
        stack.pop()
    stack.append([i,arr[i]])
    while stack and (i-stack[0][0])>(l-1):
        stack.popleft()
    print(stack[0][1],end=' ')
