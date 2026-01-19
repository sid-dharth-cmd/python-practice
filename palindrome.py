str = input("Enter a string: ").lower().replace(" ", "")
if str == str[::-1]:
    print(f"palindrome.")
else:
    print(f"not palindrome.")