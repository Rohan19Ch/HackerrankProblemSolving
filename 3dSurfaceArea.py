def surfaceArea(A):
    a = [[0] * (len(A[0]) + 2)]
    for row in A:
        a.append([0] + row + [0])
    a.append([0] * (len(A[0]) + 2))
    for i in a:
    	print(i)
    ans = len(A) * len(A[0]) * 2
    for i in range(1, len(a)):
        for j in range(1, len(a[i])):
            ans += abs(a[i][j] - a[i-1][j])
            ans += abs(a[i][j] - a[i][j-1])
    return ans
a = [[1,3,4], [2,2,3], [1,2,4]]
print(surfaceArea(a))