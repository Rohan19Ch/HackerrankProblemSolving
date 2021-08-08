def birthday(s, d, m):
    l = []
    for i in range(0, len(s)-m+1):
        l.append([s[j] for j in range(i,i+m)])
    print(l)
    Vals = []
    for j in l:
    	sum = 0
    	for i in j:
    		sum+=i
    	Vals.append(sum)
    print(Vals)
    count = 0
    for j in Vals:
    	if j == d:
    		count+=1
s = [1,2,1,3,2]
d = 3
m = 2
birthday(s,d,m)