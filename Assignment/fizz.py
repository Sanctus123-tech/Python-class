# FizzBuzz from 1 to 30

for i in range(1, 31):   # Loop from 1 to 30
    if i % 3 == 0 and i % 5 == 0:   # Divisible by both 3 and 5
        print("fizzbuzz")
    elif i % 3 == 0:   # Divisible by 3
        print("fizz")
    elif i % 5 == 0:   # Divisible by 5
        print("buzz")
    else:
        print(i)
