arr=list(map(int,input().split()))

if arr==sorted(arr):
    print("ascending")
elif arr[::-1]==sorted(arr):
    print("descending")
else:
    print("mixed")