
#Written by Adam Sadowsky

start = input("Would you like to start? (y/n) ")
total = 0

#Loops as long as user enters y or Y
while start == "y" or start == "Y":
    num1 = float(input("Enter a number: "))
    operator = input("Enter an operator: ")
    num2 = float(input("Enter a number: "))

    #Checks for valid operators
    if operator == "-":
        total = num1 - num2
    elif operator == "+":
        total = num1 + num2
    elif operator == "*":
        total = num1 * num2
    elif operator == "/":
        if num2 == 0:
            #Handles case for division by 0
            print("Cannot divide a number by zero.")
            continue
        total = num1/num2
    else:
        #Handles case for when an invalid operator is entered
        print(f"{operator} is not a valid operator.")

    #Outputs the result of users entries
    print(f"Result: {total}")

    start = input("Would you like to continue? (y/n) ")

    #Terminates program if user enters n or N
    if start == "n" or start == "N":
        print("Goodbye")
