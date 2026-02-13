s1 = {4, 6, 2, 7, 4, 8, 9, 3}
s2 = {4, 6, 2, 8, 4, 9, 5}
res = set()
for i in s2: 
    if i not in s1:
        res.add(i)
for i in s1:
    if i not in s2:
        res.add(i)
print(res)

# s1 ^ s2