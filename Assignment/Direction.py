"""
This code is to help a user locate the direction of a point which they have selected
"""



Location1 = "Emene"
Location2 = "Abakpa"

print("Please select a location(Emene or Abakpa):")
sellocation = input()
if sellocation  == Location1:
    print("Enter a tricycle going to Holy Ghost then enter a bus that is heading towards Emene")
elif sellocation == Location2:
 print("Enter a bus going to Abakpa then enter a tricycle that is heading towards Abakpa")
else:
    print("Invalid location selected. Please choose either Emene or Abakpa.")
