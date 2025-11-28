# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [i for i in numbers if i <= 0]
print(negatives_and_zero)

# 2. Flatten the following list of lists of lists to a one dimensional list:
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sub in list_of_lists for inner in sub for num in inner]
print(flattened)

# 3. Using list comprehension create the following list of tuples:
result = [
    (i, 1, i, i**2, i**3, i**4, i**5)
    for i in range(11)
]
print(result)

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]
print(formatted)

# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]
print(dict_list)

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Erwin', 'Frias')], [('Erendira', 'Hernandez')], [('Oscar', 'Frias')], [('Cesar', 'Frias')]]
full_names = [
    f"{first} {last}"
    for [(first, last)] in names
]
print(names)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope)

y_intercept = lambda m, x, y: y - m * x
print(y_intercept)

linear_info = lambda x1, y1, x2, y2: {
    'slope': (y2 - y1) / (x2 - x1),
    'intercept': y1 - ((y2 - y1) / (x2 - x1)) * x1
}
print(linear_info)