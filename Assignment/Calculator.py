# """
# This is a code to print out the;
# Sum of two numbers
# Difference of two numbers
# Product of two numbers
# Quotient of two numbers
# """
# def calculator():
#  p

# print("What is your first number?")
# num1 = int(input("Number 1: "))

# print("What is your second number?")
# num2 = int(input("Number 2: "))

# print("Which calculation would you like to perform?")
# calc = str(input("Enter 'add', 'sub', 'mult', or 'div': "))

# sum = num1 + num2
# if calc.lower() == 'add': 
#  print(f"This is the sum of the two numbers; {sum}") #addition

# sub = num1 - num2
# if calc.lower() == 'sub':
#  print(f"This is the difference of the two numbers; {sub}") #subtraction

# mult = num1 * num2
# if calc.lower() == 'mult':
#  print(f"This is the product of the two numbers; {mult}") #multiplication

# div = num1 / num2
# if calc.lower() == 'div':
#  print(f"This is the quotient of the two numbers; {div}") #division

# if calc.lower() == '':
#  print(f"Invalid selection !!!! ")

"""
This program performs:
- Sum of two numbers
- Difference of two numbers
- Product of two numbers
- Quotient of two numbers
"""

while True:
    print("What is your first number?")
    num1 = int(input("Number 1: "))

    print("What is your second number?")
    num2 = int(input("Number 2: "))

    print("Which calculation would you like to perform?")
    calc = input("Enter 'add', 'sub', 'mult', or 'div': ").lower()

    if calc == 'add':
        print(f"This is the sum of the two numbers: {num1 + num2}")  # addition
    elif calc == 'sub':
        print(f"This is the difference of the two numbers: {num1 - num2}")  # subtraction
    elif calc == 'mult':
        print(f"This is the product of the two numbers: {num1 * num2}")  # multiplication
    elif calc == 'div':
        if num2 != 0:
            print(f"This is the quotient of the two numbers: {num1 / num2}")  # division
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid selection !!!!")

    again = input("Do you want to continue? (yes(y)/no(n)): ").lower()
    if again != 'y':
        print("Then get out😂!")
        break
