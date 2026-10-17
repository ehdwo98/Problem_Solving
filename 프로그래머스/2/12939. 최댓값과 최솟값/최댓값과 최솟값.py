def solution(s):
    answer = ''
    tmp=list(map(int,s.split()))
    # print(tmp)
    s_min=str(min(tmp))
    s_max=str(max(tmp))
    # print(s_min,s_max)
    answer+=(s_min+" "+s_max)
    return answer