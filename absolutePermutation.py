def absolutePermutation(n, k):
	perm = []
	if k == 0:
		for i in range(n):
			perm.append(i+1)
		return perm
	elif (n/k)%2!=0:
		return [-1]
	else:
		flag = True
		for i in range(1, n+1):
			if flag:
				perm.append(i+k)
			else:
				perm.append(i-k)
			if i%k ==0:
				if flag:
					flag = False
				else:
					flag = True
		return perm
print(absolutePermutation(100, 2))