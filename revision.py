name = "a"
# age = 22
# school = "Aptech"
# course = "python"
# country = "Nigeria"
# print(f"My name is {name}, I am {age} years old, I study {course} at {school} in {country}.")
def greet():
    name = "b"
    print("this is for local"+name)
    greet()

    print("this is for global"+name)