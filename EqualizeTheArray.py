def equalizeArray(arr):
    maxim = max(arr)
    length = len(arr)
    l = [0 for i in range(maxim+1)]
    for i in arr:
        l[i-1] += 1
    count = max(l)
    return (length-count)