"""
this program checks if a number inputed is positive or negative
"""

while True:   
    num = int(input("Enter a number: "))
    if num < 0:   
        print("Program ended because you entered a negative number.")
        break
    else:
        print("You entered:", num)
