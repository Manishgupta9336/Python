arr = [45,25,26,58,74,9,8]
res = arr[0]
for i in range(len(arr)):
    if arr[i] > res:
        res = arr[i]
print(res)
