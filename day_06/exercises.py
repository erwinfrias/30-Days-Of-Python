# =============================
# Exercises: Level 1
# =============================

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Marcos', 'Hugo')
sisters = ('Saira', 'Karen')
print(brothers)
print(sisters)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# 4. How many siblings do you have?
siblings_leng = len(siblings)
print(siblings_leng)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Felipe', 'Sandra')
family_members = siblings + parents
print(family_members)

# =============================
# Exercises: Level 2
# =============================

# 1. Unpack siblings and parents from family_members
*unpacked_siblings, father, mother = family_members
print('Siblings:', unpacked_siblings)
print('Father:', father)
print('Mother:', mother)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to food_stuff_tp
fruits = ('Apple', 'Pineaple', 'Orange', 'Strawberry')
vegetables = ('Tomato', 'Cucumber', 'Carrot', 'Avocado')
animal_products = ('Milk', 'Egg', 'Cheese', 'Meat')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[mid_index-1:mid_index+1]
else:
    middle_items = food_stuff_lt[mid_index]
print('Middle item(s):', middle_items)

# 5. Slice out the first three items and the last three items from food_staff_lt list
print('First three items:', food_stuff_lt[:3])
print('Last three items:', food_stuff_lt[-3:])

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)