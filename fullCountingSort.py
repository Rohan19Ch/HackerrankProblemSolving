def countSort(arr):
    length = len(arr)
    maxim = int(arr[0][0])
    for i in range(length):
        arr[i][0] = int(arr[i][0])
    for i in range(length//2):#replace as per question
        arr[i][1] = "-"
    for i in range(length):#to find maximum index
        if arr[i][0] > maxim:
            maxim = arr[i][0]
    decoy2 = [[]]*(maxim+1)
    print(type(decoy2))
    decoy = [[] for i in range(maxim+1)]
    # [[-,-], [], [], [], [], [], [-]]
    print(type(decoy))
    for i in range(length):
        key = arr[i][1]
        index = arr[i][0]
        decoy[index].append(key)
        print(decoy)
    str1 = ""
    for i in decoy:
        for j in i:
            str1 += j
            str1 += " "
    str1.strip()
    print(str1)
    
arr = [["0","ab"],["6","cd"],["0","ef"],["6","gh"],["4","ij"],["0","ab"],["6","cd"],["0","ef"],["6","gh"],["0","ij"],["4","that"],["3","be"],["0","to"],["1","be"],["5","question"],["1","or"],["2","not"],['4',"is"],['2',"to"],['4',"the"]]
countSort(arr)