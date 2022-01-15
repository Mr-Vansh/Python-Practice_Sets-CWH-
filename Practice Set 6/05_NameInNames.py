# Hardcoded names in the "NAMES"
names = ["Vansh" , "Vedant" , "Sahil" , "Aniket" , "Rohti", "Aryan"]

# Taking user input & storing in "NAME"
name = input("Enter name : ")

if name in names:
    print("Provided name is present in the list")
else:
    print("Provided name is NOT present in the list")