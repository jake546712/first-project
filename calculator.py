print("SIMPLE CALCULATOR!!!!")
line = input("Enter the calculation (example: 7 * 9, 8 + 2,...):").strip()
part = line.split()
if len(part) == 3:
    try:
        num1= float(part[0])
        oper = (part[1])
        num2 = float(part[2])

        if oper == "x":
            print("Answer:", num1*num2)
        elif oper == "+":
            print("Answer:", num1+num2)
        elif oper == "-":
            print("Answer:", num1-num2)
        elif oper == ":":
            if num2 == 0:
                print("Error!!")
            else:
                print("Answer:", num1/num2)
        else:
            print("only + , - , x , :")
    except:
        print("Error")
else:
    print("Right numbers")
