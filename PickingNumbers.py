def pickingNumbers(a):
	l = []
	for i in a:
		l1 = []
		for j in a:
			if j == i or j-i == 1:
				l1.append(j)
		print(l1)
		l.append(l1)
	print(l)
	l.sort(key = len)
	print(l)
	return len(l[-1])
arr = [4,6,5,3,3,1]
print(pickingNumbers(arr))