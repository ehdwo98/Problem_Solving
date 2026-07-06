def solution(tickets):
    answer = []
    tickets.sort()
    n=len(tickets)
    visited=[0]*n
    def dfs(path):
        if len(path)==n+1:
            answer.extend(path)
            return True
        cur=path[-1]
        for i in range(n):
            if not visited[i] and cur==tickets[i][0]:
                visited[i]=1
                if dfs(path+[tickets[i][1]]):
                    return True
                visited[i]=0
        return False
    dfs(['ICN'])
    return answer