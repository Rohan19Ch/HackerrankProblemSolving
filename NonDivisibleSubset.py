def nonDivisibleSubset(k, s):
	print(s)
	remainder = [0]*k
	for i in s:
		print(i)
		remainder[i%k] += 1
	print(remainder)
	maxnum = 0
	maxnum += min(remainder[0], 1)
	print(maxnum)
	if k%2 == 0:
		maxnum += min(remainder[k//2], 1)
	print(maxnum)
	for i in range(1, k//2+1):
		if i != k-i:
			maxnum += max(remainder[i], remainder[k-i])
		print(maxnum)
	return maxnum
k = 4
s = [19, 10, 12, 10, 24, 25, 22]
print(nonDivisibleSubset(k,s))