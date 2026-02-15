def findFact(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {findFact(n)}")