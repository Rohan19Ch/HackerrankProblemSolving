def segregate0_1(arr):
    print(len(arr))
    i = 0
    j = len(arr)-1
    while i<j:
        while arr[i] == 0:
            i+=1
        while arr[j] == 1:
            j-=1
        if i<j:
            arr[i] = 0
            arr[j] = 1
            
            i+=1
            j-=1
    return arr
arr = [0,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0]
result = segregate0_1(arr)
print(len(result))
print(result)