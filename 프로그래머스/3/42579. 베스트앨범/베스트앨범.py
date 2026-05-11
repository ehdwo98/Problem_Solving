def solution(genres, plays):
    answer = []
    dic=dict()
    dic2=dict()
    for i,(genre,play) in enumerate(zip(genres,plays)):
        # print(i,genre,play)
        if genre not in dic:
            dic[genre]=list()
            dic2[genre]=0
        dic[genre].append([play,i])
        dic2[genre]+=play
    print(dic)
    # print(dic2)
    tmp=sorted(list(dic2.items()),key=lambda x:-x[1])
    print(tmp)
    for a,b in tmp:
        # print(a,b)
        tmp2=sorted(dic[a],key=lambda x:(-x[0],x[1]))[:2]
        for c,d in tmp2:
            answer.append(d)
            
    return answer