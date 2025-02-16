import sys
# input=sys.stdin.readline

while 1:
    try:
        cnt1,cnt2,cnt3,cnt4=0,0,0,0
        arr=input()
        for a in arr:
            if a.islower()==1:
                cnt1+=1
            elif a.isupper()==1:
                cnt2+=1
            elif a.isnumeric()==1:
                cnt3+=1
            elif a.isspace()==1:
                cnt4+=1
        print(cnt1,cnt2,cnt3,cnt4)
    except EOFError:
        break