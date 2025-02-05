import sys
input=sys.stdin.readline

scores=list(int(input())for _  in range(8))
res=sorted(scores,reverse=True)[:5]

print(sum(res))
ans=list()
for r in res:
    ans.append(scores.index(r)+1)
print(*sorted(ans))