n = int(input("Enter a year: "))
print("Leap year" if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0) else "Not a leap year.")