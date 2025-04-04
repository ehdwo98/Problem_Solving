import sys
input=sys.stdin.readline

arr=input().rstrip()

ans=0
for a in arr:
    for idx, words in enumerate(['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']):
        if a in words:
            ans+=idx+3
print(ans)