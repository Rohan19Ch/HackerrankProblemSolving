l=[1,2,2,4,4,5,6,7,7,8,8,8,8]
hash = [0]*(max(l)+1)
for i in l:
    hash[i]+=1
print(hash)
print(max(hash))