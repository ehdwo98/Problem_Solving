from collections import deque

def solution(bridge_length, weight, truck_weights):
    l=bridge_length
    answer=0
    bq=deque(list(0 for _ in range(l)))
    tq=deque(truck_weights)
    # 초기 0,0
    # 0,7
    # 7,0
    
    while tq:
        answer+=1
        bq.popleft()
        if sum(bq)+tq[0]<=weight:
            t=tq.popleft()
            bq.append(t)
        else:
            bq.append(0)
    answer+=bridge_length
            
    return answer