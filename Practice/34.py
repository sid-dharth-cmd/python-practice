s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {3, 4, 5}
subset = True 
for i in s2:
    if i not in s1:
        subset = False
        break
print("s2 is subset of s1." if subset else "s2 is not a subset of s1.")