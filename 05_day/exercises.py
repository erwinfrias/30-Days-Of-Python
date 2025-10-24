# 1. Declare an empty list
empty_list = []
print(empty_list)

# 2. Declare a list with more than 5 items
items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig']
print(items)

# 3. Find the length of your list
print(len(items))

# 4. Get the first item, the middle item and the last item of the list
first_item = items[0]
middle_item = items[len(items)//2]
last_item = items[-1]
print(first_item, middle_item, last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Erwin Frias', 30, 1.75, 'Single', 'Mexico City']
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[1] = 'YouTube'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Netflix')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'OpenAI')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

# 15. Check if a certain company exists in the it_companies list.
print('Google' in it_companies)
print('OpenAI' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies)//2
if len(it_companies) % 2 == 0:
    print(it_companies[middle_index-1:middle_index+1])
else:
    print(it_companies[middle_index])

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
middle_index = len(it_companies)//2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index-1:middle_index+1]
else:
    del it_companies[middle_index]
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists: front_end + back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. After joining, insert Python and SQL after Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# 28. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
min_age, max_age = min(ages), max(ages)
print('Min:', min_age, 'Max:', max_age)

# 29. Add the min age and the max age again to the list
ages.extend([min_age, max_age])
print(ages)

# 30. Find the median age (middle value)
length = len(ages)
if length % 2 == 0:
    median = (ages[length//2 - 1] + ages[length//2]) / 2
else:
    median = ages[length//2]
print('Median:', median)

# 31. Find the average age
average = sum(ages) / len(ages)
print('Average:', average)

# 32. Find the range of the ages
range_ages = max_age - min_age
print('Range:', range_ages)

# 33. Compare (min - average) and (max - average)
print('abs(min - avg):', abs(min_age - average))
print('abs(max - avg):', abs(max_age - average))

# 34. Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_index = len(countries)//2
if len(countries) % 2 == 0:
    print(countries[middle_index-1:middle_index+1])
else:
    print(countries[middle_index])

# 35. Divide the countries list into two equal lists if even, if not, one more country for the first half
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]
print('First half:', first_half)
print('Second half:', second_half)

# 36. Unpack the first three countries and the rest as scandic countries
china, russia, usa, *scandic = countries
print('China:', china)
print('Russia:', russia)
print('USA:', usa)
print('Scandic countries:', scandic)