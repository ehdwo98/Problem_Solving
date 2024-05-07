def solution(n, m, section):
    answer = 0
    
    len_sec=section[-1]-section[0]+1
    
    if len(section)==1:
        return 1
    else:    
        cnt=1
        sum_sec=section[0]+m-1
        for i in range(len(section)):
            if sum_sec>=section[i]:
                continue
            else:
                sum_sec=section[i]+m-1
                cnt+=1
            if sum_sec>section[-1]:
                break
                
    return cnt