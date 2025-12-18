#Level 3 — Name cleanup + empty-name rejection
#Goal: Learn input cleaning and basic validation.

print("Welcome to the People Registry")
print("-------------------------------")
print("Hello, this Applications asks for your name and age and will add 1 to your current age")
name = input("Enter your Name:").lstrip().title()
age = int(input("Enter your Age:"))

if name:
    print("---Profile Card----")
    print("")
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Age next year: {age+1}")
else:
    print("error")
  

    





