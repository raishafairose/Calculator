def calculator():
    print("Select an operation : ")
    print("1. Addition")
    print("2. subtraction")
    print("3. Multiplication")
    print("4. Division ")

    answer = input("Enter your desired operation no. (1-4) : ")

    num1 = float(input("Enter first value : "))
    num2 = float(input("Enter second value : "))

    if answer == "1":
        result = num1 + num2
        print("Your result is:", str(result))

    elif answer == "2":
        result = num1 - num2
        print("Your result is:", str(result))

    elif answer == "3":
        result = num1 * num2
        print("Your result is:",str(result))

    elif answer == "4":
        try:
           result = num1 / num2
           print("Your result is:", str(result))
        except ZeroDivisionError :
           print("Can't devided by zero")

    else:
        print("Invalid")
calculator()







