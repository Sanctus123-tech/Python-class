# """
# This
# """

# import time  

# for count in range(10, 0, -1):   
#     print(count)
#     time.sleep(1)   

# print("Time is up ")




import time

beginning = 10   # starting number
end = 0          # stopping point (just before this number)

for number in range(beginning, end, -1):   # from 10 down to 1
    print(number)
    time.sleep(1)

print("Time is up!")
