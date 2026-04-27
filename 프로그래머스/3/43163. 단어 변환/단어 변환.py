# 가장 짧은 변환과정 -> BFS탐색
from collections import deque

def solution(begin, target, words):
    answer = 0
    visited=[0]*(len(words)+1)
    q=deque()
    visited[-1]=1
    q.append([begin,-1])
    while q:
        p,idx=q.popleft()
        # print("init:",p,idx)
        for w in range(len(words)):
            cmd=0
            for i in range(len(p)):
                x=p[0:i]+p[i+1::]
                y=words[w][0:i]+words[w][i+1::]
                if x==y and not visited[w]:
                    visited[w]=visited[idx]+1
                    # print(x,y)
                    # print(p,words[w],visited[w])
                    if words[w]==target:
                        return visited[w]-1
                    cmd=1
            if cmd:
                q.append([words[w],w])
    return answer