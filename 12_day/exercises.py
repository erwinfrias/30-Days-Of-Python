import random
import string

# =============================
# Exercises: Level 1
# =============================

# 1. Writ a function which generates a six digit/character random_user_id.
def random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. 
def user_id_gen_by_user():
    num_chars = int(input("Number of characters per ID: "))
    num_ids = int(input("Number of IDs to generate: "))

    chars = string.ascii_letters + string.digits
    ids = []

    for _ in range(num_ids):
        new_id = ''.join(random.choice(chars) for _ in range(num_chars))
        ids.append(new_id)
    return "\n".join(ids)

print(user_id_gen_by_user())

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

# =============================
# Exercises: Level 2
# =============================

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        hex_value = ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hex_colors.append(f"#{hex_value}")
    return hex_colors

print(list_of_hexa_colors(2))

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print(list_of_rgb_colors(5))

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, n):
    color_type = color_type.lower()

    if color_type == "hexa":
        return list_of_hexa_colors(n)
    elif color_type == "rgb":
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."

print(generate_colors('hexa', 3))
print(   generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

# =============================
# Exercises: Level 3
# =============================

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    result = lst[:]
    random.shuffle(result)
    return result

print(shuffle_list)

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())