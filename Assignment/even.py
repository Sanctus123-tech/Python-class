"""
this program will take a number as input and check if it is odd or even
"""

print("Welcome to the Odd or Even game!")

# Ask user for a number
number = int(input("Enter a number: "))

# Check if it's odd or even
if number % 2 == 0:
    print(f"{number} is Even ")
else:
    print(f"{number} is Odd ")
