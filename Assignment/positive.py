# Positive only program

while True:   # Keep running
    num = int(input("Enter a number: "))
    if num < 0:   # If negative, stop
        print("Program ended because you entered a negative number.")
        break
    else:
        print("You entered:", num)
