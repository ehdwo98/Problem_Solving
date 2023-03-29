def solution(sizes):
    sizes.sort(reverse=True)
    max1=sizes[0][0]
    
    sizes.sort(key= lambda x: x[1], reverse=True)
    max2=sizes[0][1]
    
    if max1>max2:
        sizes.sort(reverse=True)
        max1=sizes[0][0]
        max2=sizes[0][1]
    else:
        max1=sizes[0][1]
        max2=sizes[0][0]
    print(sizes)    
    for i in sizes:
        [r,c]=i
        if max2 < r and max2 < c:
            if r<c:
                max2=r
            else:
                max2=c
    print(max2)
    
    answer = max1*max2
    return answer