def findDigits(n):
	count = 0
	for i in str(n):
		try:
			if n%int(i) == 0:
				count += 1
		except ZeroDivisionError:
			continue
	print(count)
findDigits(654134454)