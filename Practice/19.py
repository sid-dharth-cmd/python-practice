str = input("Enter a string: ")
freq = {}
for ch in str:
    if ch != " ":
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
max_ch = ""
ch_cnt = 0
for ch in freq:
    if freq[ch] > ch_cnt:
        ch_cnt = freq[ch]
        max_ch = ch
print(f"Most frequent character is {max_ch}.")
print(f"Frequency: {ch_cnt}")