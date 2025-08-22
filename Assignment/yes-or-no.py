# Simple Yes or No program

while True:
    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice == "y":
        print("Program continues...")
    elif choice == "n":
        print("Program ended.")
        break
    else:
        print("Invalid input. Please type y or n.")
