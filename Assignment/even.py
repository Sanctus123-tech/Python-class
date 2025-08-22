"""
this program will take a number as input and check if it is odd or even
"""

print("Welcome to the Odd or Even game!")


number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is Even ")
else:
    print(f"{number} is Odd ")
