import math

def solution(progresses, speeds):
    answer = []
    arr=list(zip(progresses, speeds))
    i=0
    while 1:
        p,s=arr[i]
        res=math.ceil((100-p)/s)
        cnt=1
        cmd=1
        if i==len(arr)-1:
            print("Last",i)
            answer.append(cnt)
            break
        else:
            for j in range(i+1,len(arr)):
                np,ns=arr[j]
                nres=math.ceil((100-np)/ns)
                if res>=nres:
                    cnt+=1
                else:
                    print(i,j)
                    i=j
                    cmd=0
                    answer.append(cnt)
                    break
        if cmd:
            answer.append(cnt)
            break
    return answer