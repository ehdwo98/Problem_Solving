def solution(park, routes):
    answer = []
    
    h=len(park)
    w=len(park[0])
    
    for i in range(h):
        for j in range(w):
            if park[i][j]=='S':
                x,y=i,j
    print(x,y)
    for route in routes:
        direction,distance=route.split()
        direction=str(direction)
        distance=int(distance)
        c=1
        if direction=='E':
            for i in range(1,distance+1):
                if y+i<=w-1:
                    if park[x][y+i]=='O':
                        pass
                    elif park[x][y+i]=='X':
                        c=0
                        break
                else:
                    c=0
                    break
            if c:
                y+=distance
        elif direction=='W':
            for i in range(1,distance+1):
                if y-i>=0:
                    if park[x][y-i]=='O':
                        pass
                    elif park[x][y-i]=='X':
                        c=0
                        break
                else:
                    c=0
                    break
            if c:
                y-=distance
        elif direction=='N':
            for i in range(1,distance+1):
                if x-i>=0:
                    if park[x-i][y]=='O':
                        pass
                    elif park[x-i][y]=='X':
                        c=0
                        break
                else:
                    c=0
                    break
            if c:
                x-=distance
        elif direction=='S':
            for i in range(1,distance+1):
                if x+i<=h-1:
                    if park[x+i][y]=='O':
                        pass
                    elif park[x+i][y]=='X':
                        c=0
                        break
                else:
                    c=0
                    break
            if c:
                x+=distance
    
    answer=[x,y]
    print(answer)
    return answer