# Adults only program

while True:   # Keep asking until above 18
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Welcome, you are an adult!")
        break
    else:
        print("Sorry, you are too young. Try again.")
