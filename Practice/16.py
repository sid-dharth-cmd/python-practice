str = input("Enter a string: ")
new = ""
for ch in str:
    if ch != " ":
        new += ch
print("Palindrome" if new == new[::-1] else "Not palindrome")