str = input("Enter a sentence: ").split()
freq = {}
for i in str:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)