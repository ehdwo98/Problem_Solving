def solution(arr):
    ans=[]
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            ans.append(arr[i])
        if i+1==len(arr)-1:
            ans.append(arr[i+1])
    return ans