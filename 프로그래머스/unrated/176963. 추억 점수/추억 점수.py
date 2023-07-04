def solution(name, yearning, photo):
    answer = []
    
    d={name[i]:yearning[i] for i in range(len(name))}
    
    print(d)
    
    
    for p in photo:
        sum=0
        for i in p:
            if i in name:
                sum+=d[i]
        answer.append(sum)
    
    return answer