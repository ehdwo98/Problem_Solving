def solution(p, c):
    
    d={s:i for i,s in enumerate(p)}
    
    for c in c:
        idx=d[c]
        p[idx-1],p[idx]=p[idx],p[idx-1]
        d[p[idx-1]],d[p[idx]]=d[p[idx]],d[p[idx-1]]
        
    
    return p