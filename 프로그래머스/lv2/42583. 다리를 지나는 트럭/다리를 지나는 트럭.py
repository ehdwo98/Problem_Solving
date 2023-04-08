from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q=deque(truck_weights)
    while(q):
        if len(q)<=bridge_length and sum(q)<=weight:
            return bridge_length+len(q)
        if len(q)<=bridge_length and sum(q)>weight:
            
        if len(q)>bridge_length and sum(q)>weight:
            p=q.popleft()
            if weight-p>=q[0] and len(q)>1:
                answer--
    return answer