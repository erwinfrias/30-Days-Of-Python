countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Erwin', 'Erendira', 'Eliel', 'Eilam']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# =============================
# Exercises: Level 1
# =============================

# 1. Explain the difference between map, filter, and reduce.
print('Map: Transforms each element to create a new array.')
print('Filter: Creates a new array by selecting elements that meet a condition.')
print('Reduce: Accumulates all elements into a single value.')

# 2. Explain the difference between higher order function, closure and decorator
print('Higher-Order Function: A general concept describing functions that operate on or return other functions.')
print('Closure: A specific phenomenon where an inner function retains access to variables from its enclosing scope, even after the enclosing scope has exited.')
print('Decorator: A specific application of higher-order functions and closures, providing a concise syntax to wrap and modify functions or methods. Decorators leverage closures to store and access information about the decorated function and its environment.')
    
# 3. Define a call function before map, filter or reduce, see examples.
def square(x):
    return x * 2

list(map(square, numbers))

# 4. Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# 5. Use for to print each name in the names list.
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
for number in numbers:
    print(number)

# =============================
# Exercises: Level 2
# =============================

# 1. Use map to create a new list by changing each country to uppercase in the countries list
upper_countries = list(map(str.upper, countries))
print(upper_countries)

# 2. Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# 3. Use map to change each name to uppercase in the names list
upper_names = list(map(str.upper, names))
print(upper_names)

# 4. Use filter to filter out countries containing 'land'.
land_countries = list(filter(lambda c: 'land' in c.lower(), countries))
print(land_countries)

# 5. Use filter to filter out countries having exactly six characters.
six_char_countries = list(filter(lambda c: len(c) == 6, countries))
print(six_char_countries)

# 6. Use filter to filter out countries containing six letters and more in the country list.
six_plus_char_countries = list(filter(lambda c: len(c) >= 6, countries))
print(six_plus_char_countries)

# 7. Use filter to filter out countries starting with an 'E'
countries_with_e = list(filter(lambda c: c.startswith('E'), countries))
print(countries_with_e)

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

result = reduce(
    lambda a, b: a + b,
    filter(lambda x: x > 20,
        map(lambda x: x ** 2, numbers)
    )
)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

# 10. Use reduce to sum all the numbers in the numbers list.
total = reduce(lambda a, b: a + b, numbers)
print(total)

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence = reduce(lambda a, b: a + ', ' + b, countries[:-1])
sentence += f", and {countries[-1]} are north European countries"
print(sentence)

# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern):
    return [c for c in countries if pattern.lower() in c.lower()]

# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def categorize_countries(pattern):
    return [c for c in countries if pattern.lower() in c.lower()]

# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries[:10]

# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries[-10:]

# =============================
# Exercises: Level 3
# =============================