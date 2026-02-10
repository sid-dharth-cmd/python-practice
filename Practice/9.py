mark = int(input("Enter the mark of the student: "))
m =  mark // 10
match m:
    case 10:
        print("O grade.")
    case 9:
        print("O grade")
    case 8:
        print("A grade.")
    case 7:
        print("B grade.")
    case 6:
        print("C grade.")
    case 5: 
        print("D grade.")
    case 4:
        print("E grade.")
    case _:
        print("Fail.")