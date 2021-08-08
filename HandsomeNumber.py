x = 5801001

if x//9 == 0:
	print(x)
else:
	l = []
	l2 = []
	for i in str(x):
		l.append(int(i))
		l2.append(int(i))
	print(l)

	for i in range(len(l)-1,0, -1):
		print(l[i], l[i-1])
		print(l2[i], l2[i-1])
		if (l[i]%2 == 0 and l[i-1]%2 == 0) or (l[i]%2 !=0 and l[i-1]%2 != 0):
			if l[i-1]!= 0:
				l[i-1] -= 1
		if (l2[i]%2 == 0 and l2[i-1]%2 == 0) or (l2[i]%2 !=0 and l2[i-1]%2 != 0):
			if l2[i-1]!= 9:
				l2[i-1] += 1
	print(l)
	print(l2)
