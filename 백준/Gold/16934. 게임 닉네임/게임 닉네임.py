import sys
input=sys.stdin.readline

dic=dict()
pre=set()

n=int(input())

for _ in range(n):
    nic=input().rstrip()
    if nic in dic.keys():
        dic[nic]+=1
        print(nic+str(dic[nic]))
    else:
        dic[nic]=1
        s=''
        c=1
        for i in range(len(nic)):
            s+=nic[i]
            if s not in pre:
                print(s)
                c=0
                break
        if c:
            print(nic)
        s=''
        for i in range(len(nic)):
            s+=nic[i]
            pre.add(s)