def find(n,networks):
    if networks[n]!=n:
        networks[n]=find(networks[n],networks)
    return networks[n]

def solution(n, computers):
    print(computers)
    answer = 0
    networks=list(_ for _ in range(n))
    for i in range(n):
        for j in range(i+1,n):
            # print(networks)
            if computers[i][j]==1:
                fi=find(i,networks)
                fj=find(j,networks)
                if fi<fj:
                    networks[fj]=fi
                else:
                    networks[fi]=fj
    ans=set(list(find(x,networks) for x in range(n)))
    # print(ans)
    answer=len(ans)      
    return answer