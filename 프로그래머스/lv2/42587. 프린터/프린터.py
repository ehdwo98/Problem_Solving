from collections import deque

def solution(priorities, location):
    answer = 0
    q=deque(priorities)
    idx=[x for x in range(len(priorities))]
    
    while(q):
        if q[0]==max(q):
            q.popleft()
            x=idx.pop(0)
            answer+=1
            if x==location:
                return answer
        else:
            p=q.popleft()
            x=idx.pop(0)
            q.append(p)
            idx.append(x)