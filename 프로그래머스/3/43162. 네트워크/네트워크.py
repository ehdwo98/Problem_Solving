def find(num,networks):
    if networks[num]!=num:
        return find(networks[num],networks)
    return num

def solution(n, computers):
    networks=list(_ for _ in range(n))
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                fi=find(i,networks)
                fj=find(j,networks)
                if fi<fi:
                    networks[fj]=fi
                else:
                    networks[fi]=fj
    answer=len(set(find(x,networks) for x in range(n)))
    return answer