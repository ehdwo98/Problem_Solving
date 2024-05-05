def solution(park, routes):
    answer = []
    
    h=len(park)
    w=len(park[0])
    
    for i in range(h):
        for j in range(w):
            if park[i][j]=='S':
                x,y=i,j
    
    D={'E':[0,1],'W':[0,-1],'N':[-1,0],'S':[1,0]}#딕셔너리 형태로 하면 반복작업 피할 수 있음.
    
    for route in routes:
        direction,distance=route.split()
        direction=str(direction)
        distance=int(distance)
        c=1
        dx,dy=D[direction]
        for i in range(1,distance+1):
            nx,ny=x+dx*i,y+dy*i
            if 0<=nx<h and 0<=ny<w:
                if park[nx][ny]=='O':
                    pass
                elif park[nx][ny]=='X':#else로만 하면 안됌.
                    c=0
                    break
            else:
                c=0
                break
        if c:
            x=x+dx*distance
            y=y+dy*distance
            
    print(x,y)
    answer=[x,y]
    print(answer)
    return answer
