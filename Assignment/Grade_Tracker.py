# Student Grade Tracker

# Dictionary to store students and their grades
students = {}

# Function to add a new student
def add_student(name):
    if name not in students:
        students[name] = []
        print(f"Student '{name}' added successfully!")
    else:
        print(f"Student '{name}' already exists.")

# Function to add a grade for an existing student
def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f"Grade {grade} added for {name}.")
    else:
        print(f"Student '{name}' does not exist. Please add them first.")

# Function to calculate the average grade of a student
def calculate_average(name):
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    else:
        return 0

# Function to find the student with the highest average
def top_student():
    if not students:
        return None
    averages = {name: calculate_average(name) for name in students}
    return max(averages, key=averages.get)

# Function to display all students and their grades in a table
def display_all():
    if not students:
        print("No students found.")
        return
    print("\n--- Student Grades ---")
    print(f"{'Name':<15}{'Grades':<25}{'Average':<10}")
    print("-" * 50)
    for name, grades in students.items():
        avg = calculate_average(name)
        print(f"{name:<15}{str(grades):<25}{avg:<10.2f}")
    print("-" * 50)


# Example usage
add_student("Alice")
add_student("Bob")
add_student("Charlie")

add_grade("Alice", 85)
add_grade("Alice", 90)
add_grade("Bob", 70)
add_grade("Bob", 75)
add_grade("Charlie", 95)

display_all()

print(f"Top student: {top_student()} with average {calculate_average(top_student()):.2f}")
