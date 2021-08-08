def timeInWords(h, m):
	hours = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}
	time = ""
	if m == 30:
		print("half past " + hours[h])
	elif m == 00:
		print(hours[h]+ " o' clock")
	elif m == 15:
		print("quarter past " + hours[h])
	elif m == 45:
		print("quarter to "+ hours[h+1])
	elif m == 1:
		print("one minute past "+ hours[h])
	elif m > 30:
		m = 60-m
		if m > 19:
			print("twenty "+hours[m%10]+ " minutes to "+ hours[h+1])
		else:
			print(hours[m] + " minutes to " + hours[h+1])
	elif m<30:
		if m>19:
			print("twenty " + hours[m%10]+ " minutes past "+ hours[h])
		else:
			print(hours[m] + " minutes past " +  hours[h])
h = 1
m = 1
timeInWords(h, m)