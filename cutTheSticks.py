def cutTheSticks(arr):
	lens = []
	lens.append(len(arr))
	while True:
		minim = min(arr)
		arr = [x for x in arr if x != minim]
		if len(arr) == 0:
			break
		lens.append(len(arr))
	return lens
print(cutTheSticks([5, 4, 4, 2, 8, 7]))