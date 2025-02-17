import sys
input=sys.stdin.readline

v=int(input())
arr=input().rstrip()
cnt1,cnt2=0,0
for a in arr:
    if a=='A':
        cnt1+=1
    else:
        cnt2+=1
if cnt1>cnt2:
    print('A')
elif cnt1<cnt2:
    print('B')
else:
    print('Tie')