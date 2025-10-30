# =============================
# Exercises: Level 1
# =============================

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add ‘Twitter’ to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple companies at once
it_companies.update(['Tesla', 'Samsung', 'Intel'])
print(it_companies)

# 4. Remove one company
it_companies.remove('Facebook')   # remove raises error if item not found
print(it_companies)

# 5. Difference between remove and discard
# .remove():    Removes element, throws error if not found
# .discard():   Removes element, no error if not found

# =============================
# Exercises: Level 2
# =============================

# 1. Join A and B
A.union(B)
print(A)

# 2. A intersection B
A.intersection(B)
print(B)

# 3. Is A subset of B?
A.issubset(B)
print(A)

# 4. Are A and B disjoint?
A.isdisjoint(B)
print(A)

# 5. Join A with B and B with A
A.union(B)
B.union(A)
print(A)
print(B)

# 6. Symmetric difference between A and B
A.symmetric_difference(B)
print(B)

# 7. Delete the sets completely
del A
del B

# =============================
# Exercises: Level 3
# =============================

# 1. Convert ages to a set & compare lengths
ages_set = set(age)
len(age)        # list length
len(ages_set)   # set length

# 2. Explain difference between string, list, tuple, set
# string:   Text data
# list:     Collection that may change
# tuple:    Fixed collection
# set:      Unique items, math sets

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(len(unique_words))