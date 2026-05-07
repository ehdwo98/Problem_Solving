def solution(clothes):
    answer = 0
    dic=dict()
    for n,t in clothes:
        if t not in dic:
            dic[t]=list()
        dic[t].append(n)
    # print(dic.values())
    tmp=1
    cnt=-1
    for v in dic.values():
        # print(v)
        answer+=answer*len(v)
        answer+=len(v)
    return answer