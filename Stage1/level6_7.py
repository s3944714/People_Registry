#Level 6 — Safe age input (loop + invalid handling)
#Goal: Handle bad user input safely.
#Implement:
#Keep asking until age is a valid whole number
#If invalid, print a helpful message and re-ask
#Acceptance criteria:
#App does NOT crash on non-numeric age
#Tests:
#Age: abc
#Age: 20.5
#Age: -

import re
from datetime import date, datetime
from string import ascii_uppercase

# Start of CLI
print("Welcome to the People Registry")
print("-------------------------------")
print("Hello, this Applications asks for your name and age and will add 1 to your current age")

name = ""


while not name:
    name = input("Enter your Name:").lstrip().title()
    if not name:
        print("Try again")

age = ""
while True:
    try:
        age = int(input("Enter your Age:"))
        if age > 110:
            print("Must be a range from 0 to 100")
            continue
        if age < 1:
            print("Must be a positive number")
            continue 
        break
    except ValueError:
        print("Use numeric Digits")

        
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
            return("Child")
        elif 12 <= age < 18:
            return("Teenager")
            age >= 18
        else:
            return("Adult")

    def print(self):
        print("---Profile Card----")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Age Group:{self.age_group()}")
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





