# =============================
# Exercises: Level 1
# =============================

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return math.pi * r * r

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "All arguments must be numbers"
        total += num
    return total

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    elif month in ['september', 'october', 'november']:
        return "Autumn"
    else:
        return "Invalid month"

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1=0, y1=0, x2=1, y2=1):
    if x2 == x1:
        return "Undefined slope (vertical line)"
    return (y2 - y1) / (x2 - x1)

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1, x2]

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    return sum(range(1, n + 1))

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

# =============================
# Exercises: Level 2
# =============================

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = len([i for i in range(n + 1) if i % 2 != 0])
    return f"The number of odds are {odds}. The number of evens are {evens}."

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if not param:
        return True
    return False

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return mean(lst)

def calculate_median(lst):
    return median(lst)

def calculate_mode(lst):
    return mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return pvariance(lst)

def calculate_std(lst):
    return pstdev(lst)

# =============================
# Exercises: Level 3
# =============================
# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(15))
print(is_prime(2))

# 2. Write a functions which checks if all items are unique in the list.
def unique_items(lst):
    return len(lst) == len(set(lst))
print(unique_items([1, 2, 3, 4]))
print(unique_items([1, 2, 2, 3, 4, 8, 8]))

# 3. Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)
print(same_data_type([1, 2, 3, 4]))
print(same_data_type([1, 'two', 3, 'four']))

# 4. Write a function which check if provided variable is a valid python variable
def is_valid_variable(name):
    return name.isidentifier()
print(is_valid_variable("my_var"))
print(is_valid_variable("1variable"))
print(is_valid_variable("var-name"))