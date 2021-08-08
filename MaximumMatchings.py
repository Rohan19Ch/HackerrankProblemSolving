n = 10
a1 = [4,8,5,9,2,6,2,7,8,2]
a2 = [7,8,8,4,9,2,6,9,7,2]
lst = []
i = 0
for i in range(n):
    lst.append(a2[i] - a1[i])
    i += 1
print(lst)
hash = [0]*(max(lst)+1)
for i in lst:
    hash[i] +=1																			
print(hash)