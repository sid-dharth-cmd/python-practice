dic = {'A': 40, 'B': 44, 'C': 35, 'D': 48, 'E': 28}
key = input("Which key you wanna check for?")
try:
    dic[key]
except KeyError:
    print("Key does not exist.")
else:
    print("Key exists.")