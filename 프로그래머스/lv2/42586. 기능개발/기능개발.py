import math

def solution(progresses, speeds):
    answer = []
    tmp=[]
    for i in range(len(speeds)):
        tmp.append(math.ceil((100-progresses[i])/speeds[i]))
    #print(tmp)
    a=tmp.pop(0)
    cnt=1
    while tmp:
        if tmp[0]<=a:
            tmp.pop(0)
            cnt+=1
        else:
            a=tmp.pop(0)
            answer.append(cnt)
            cnt=1
    answer.append(cnt)
    return answer