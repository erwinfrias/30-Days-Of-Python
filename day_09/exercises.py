# =============================
# Exercises: Level 1
# =============================

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    missing_years = 18 - age
    print(f"You need {missing_years} more years to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 20 
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    year_word = "year" if diff == 1 else "years"
    print(f"You are {diff} {year_word} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    year_word = "year" if diff == 1 else "years"
    print(f"I am {diff} {year_word} older than you.")
else:
    print("We are the same age.")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# =============================
# Exercises: Level 2
# =============================

# 1. Write a code which gives grade to students according to theirs scores:
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter month: ").capitalize()

if month in ("September", "October", "November"):
    print("Autumn")
elif month in ("December", "January", "February"):
    print("Winter")
elif month in ("March", "April", "May"):
    print("Spring")
elif month in ("June", "July", "August"):
    print("Summer")
else:
    print("Invalid month")

# 3. The following list contains some fruits:
fruits = ['Apple', 'Banana', 'Strawberry', 'Orange']

new_fruit = input("Enter a fruit: ").lower()

if new_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print(fruits)

# =============================
# Exercises: Level 3
# =============================

# 1. Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Erwin',
    'last_name': 'Frias',
    'age': 31,
    'country': 'Mexico',
    'is_marred': True,
    'skills': ['HTML', 'React', 'JavaScript', 'Node', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle = len(skills) // 2
    print("Middle skill:", skills[middle])

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Person has Python skill")

skills = person['skills']

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print("He is a front end developer")
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("He is a backend developer")
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("He is a fullstack developer")
else:
    print("Unknown title")

if person['is_marred'] and person['country'] == 'Mexico':
    print(f"{person['first_name']} {person['last_name']} lives in Mexico. He is married.")