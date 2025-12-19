#Level 5 — Custom greeting (branching)
#Goal: Use if/else.
#Implement:
#A greeting that changes based on:
#First letter (A–M vs N–Z), OR
#Age range (kid/teen/adult)
#Acceptance criteria:
#Different users trigger different outputs
#Tests:
#Name: Alice vs Zane
#Age: 12, 17, 25

from datetime import date, datetime
from string import ascii_uppercase

print("Welcome to the People Registry")
print("-------------------------------")
print("Hello, this Applications asks for your name and age and will add 1 to your current age")

name = input("Enter your Name:").lstrip().title()
age = int(input("Enter your Age:"))

current_year = date.today().year
birth_year = (current_year-age)

def remain():
    current_date = datetime.now().date()
    year_end = date(current_date.year, 12, 31)
    return(year_end - current_date).days
    
days = round((current_year - birth_year) * 365.24)

alphabet = ascii_uppercase
alpha = list(alphabet)
first_letter = name[0].upper()
alphaAM = alpha[:13]
alphaMZ = alpha[13:]

class profile:
    def __init__(self, name, age, days):
        self.name = name
        self.age = age
        self.days = days
    def age_group(self,):
        if age < 12:
            print("Child")
        elif 12 <= age < 18:
            print("Teenager")
            age >= 18
        else:
            print("Adult")

    def print(self):
        print("---Profile Card----")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Age_Group:{self.age_group()}")
        print(f"Age next year:{self.age+1}")
        print(f"Age in Months:{self.age*12}")
        print(f"Age in days:{self.days}")
        
p = profile(name, age, days,)

if first_letter in alphaAM:
    print("This is the custom gretting for people A-M")
    p.print()

elif first_letter in alphaMZ:
    print("This is the custom gretting for people M-Z")
    if age < 12:
        print("Child")
    elif 12 <= age < 18:
        print("Teenager")
        age >= 18
    else:
        print("Adult")
    p.print()
else:
    print("Error")





