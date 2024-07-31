arr=list(input())

tmp=''
arr2=[]
for i in range(len(arr)):
    if arr[i]=='-' or arr[i]=='+':
        arr2.append(int(tmp))
        arr2.append(arr[i])
        tmp=''  
    else:
        tmp+=arr[i]
arr2.append(int(tmp))
#print(arr2)

cnt=0
ans=0
for i in range(len(arr2)):
    if arr2[i]=='-':
        cnt+=1
    elif arr2[i]=='+':
        continue
    else:
        if cnt==0:
            ans+=arr2[i]
        else:
            ans-=arr2[i]

print(ans)