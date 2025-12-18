#Level 2 — Pretty output (Profile card)
#Practice formatting and clean output.
print("-------------------------------")
print("Welcome to the People Registry")
print("-------------------------------")
print("Hello, this Applications asks for your name and age and will add 1 to your current age")
name = input("Enter your Name: ")
age= int(input("Enter your Age: "))
print("")
print("---Profile Card----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Age next year: {age+1}")

