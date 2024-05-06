def solution(wallpaper):
    answer = []
    
    h=len(wallpaper)
    w=len(wallpaper[0])
    
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j]=='#':
                answer.append([i,j])
    
    answer.sort()
    #print(answer)
    lux,rdx=answer[0][0],answer[-1][0]+1
    
    answer.sort(key=lambda x:x[1])
    #print(answer)
    luy,rdy=answer[0][1],answer[-1][1]+1
    
    arr=[lux,luy,rdx,rdy]
    
    
    return arr