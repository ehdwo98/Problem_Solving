from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    words=[begin]+words
    n=len(words)
    visited=[0]*n
    q=deque()
    q.append(0)
    visited[0]=1
    
    while q:
        p=q.popleft()
        print(words[p],visited[p]-1)
        if words[p]==target:
            answer=visited[p]-1
            break
        for a in range(n):
            if not visited[a]:
                cnt=0
                for i in range(len(words[0])):
                    if words[p][i]==words[a][i]:
                        cnt+=1
                if cnt==len(words[0])-1:
                    visited[a]=visited[p]+1
                    q.append(a)
    return answer