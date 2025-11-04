# 1. Create an empty dictionary called dog
dog = {}
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Tomy'
dog['color'] = 'Brown'
dog['breed'] = 'Chihuahua'
dog['legs'] = 4
dog['age'] = 5
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Cesar',
    'last_name': 'Frias',
    'gender': 'Male',
    'age': 2,
    'marital_status': 'single',
    'skills': ['HTML', 'CSS', 'JavaScript', 'Git', 'Python'],
    'city': 'Mexico',
    'address': 'Reforma'
}
print(student)

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)
print(type(skills))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('React')
student['skills'].append('Angular')
print(student)

# 7. Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)

# 8. Get the dictionary values as a list
student_values = student.values()
print(student_values)

# 9. Change the dictionary to a list of tuples using items() method
student_list = list(student.items())
print(student_list)
print(type(student_list))

# 10. Delete one of the items in the dictionary
student.popitem()
print(student)

# 11. Delete one of the dictionaries
del student
print(student)