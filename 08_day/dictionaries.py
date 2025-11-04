# Creating a Directory
person = {
    'first_name':'Erwin',
    'last_name':'Frias',
    'age':31,
    'country':'Mexico',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Reforma',
        'zipcode':'02210'
    }
}
print(person)

# Dictionary Length
print(len(person))

# Accessing Dictionary Items
print(person['first_name'])         # Erwin
print(person['country'])            # Mexico
print(person['skills'])             # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])          # JavaScript
print(person['address']['street'])  # Space street

print(person.get('city'))           # The get method returns None, which is a NoneType object data type, if the key does not exist.

# Adding Items to a Dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

# Modifying Items in a Dictionary
person['first_name'] = 'Oscar'
person['age'] = 7
print(person)

# Checking Keys in a Dictionary
print('last_name' in person)    # True
print('hobby' in person)        # False

# Removing Key and Value Pairs from a Dictionary
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the job_title
del person['is_married']        # Removes the is_married item
print(person)

# Copy a Dictionary
person_copy = person.copy()

# Getting Dictionary Keys as a List
person_keys = person.keys()
print(person_keys)

# Getting Dictionary Values as a List
person_values = person.values()
print(person_values)