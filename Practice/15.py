str = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_cnt = 0
cons_cnt = 0
special_cnt = 0
for i in str:
    if i == " ":
        continue
    elif i.isalpha: # 97 <= i >= 122
        if i in vowels:
            vowel_cnt += 1
        else:
            cons_cnt += 1
    else:
        special_cnt += 1
print(f"No. of consonants = {cons_cnt}")
print(f"No. of vowels = {vowel_cnt}")
print(f"No. of special characters = {special_cnt}")