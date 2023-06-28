def solution(n, lost, reserve):
    answer = 0
    cnt=0
    lost.sort()
    reserve.sort()
    arr=[]
    for i in lost:
        if i in reserve:
            arr.append(i)
            reserve.remove(i)
            
    for i in arr:
        lost.remove(i)
    
    for i in lost:
        if (i-1) in reserve:
            cnt+=1
            reserve.remove(i-1)
            continue
        if (i+1) in reserve:
            cnt+=1
            reserve.remove(i+1)

    answer=n-len(lost)+cnt
    
    return answer