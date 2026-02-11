str = input("Enter a sentence")
word = ""
result = ""
for ch in str:
    if ch != " ":
        word = ch + word
    else:
        result += word + " "
        word = ""
print(result)


str = input("Enter a sentence: ")
result = ""
words = str.split()
for word in words:
    rev = ""
    for ch in word:
        rev = ch + rev
    result = rev +" "
print(result.strip())


str = input("Enter a sentence: ")
result = " ".join(word[::-1] for word in str.split())
print(result)