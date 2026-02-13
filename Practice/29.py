t = (4,4,4,3,8,2,6,1,3,9,6,3,3,4,8,9,7,8,5,7,0,0)
key = int(input("Enter the key element: "))
freq = 0
for i in t:
    if i == key:
        freq += 1
print(f"frequency: {freq}")