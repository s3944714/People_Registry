#Level 4 — Age math (months)
#Goal: Basic arithmetic + variables.
#Implement:
#Display age next year
#Display age in months (age * 12)
#Optional: age in days (rough estimate)

from datetime import date, datetime

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

if name:
    print("---Profile Card----")
    print("")
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Age next year:{age+1}")
    print(f"Age in Months:{age*12}")
    print(f"Age in days:{days}")
else:
    print("error")