# Declare your age as an integer variable
age = 31

# Declare your height as a float variable
height = 1.70

# Declare a variable that stores a complex number
complex_num = 3 + 4j

# Area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is", area)

# Perimeter of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

# Rectangle area and perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

# Circle area and circumference
pi = 3.14
radius = float(input("Enter radius: "))
area = pi * radius ** 2
circumference = 2 * pi * radius
print("Area:", area)
print("Circumference:", circumference)

# Slope, x-intercept, y-intercept
m = 2
b = -2
x_intercept = 1   # x-intercept: set y = 0 => 0 = 2x - 2 => x = 1
y_intercept = -2  # y-intercept: set x = 0 => y = -2

print("Slope:", m)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# Slope and distance between points (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope:", slope)
print("Distance:", distance)

# Compare slopes
print("Slopes are equal:", m == slope)

# Solve quadratic y = x² + 6x + 9
# factorized: (x+3)^2 = 0 => x = -3
x = -3
y = x**2 + 6*x + 9
print("y =", y, "when x =", x)

# Length comparison of ‘python’ and ‘dragon’
len_python = len('python')
len_dragon = len('dragon')
print("Is length of python equal to length of dragon?", len_python == len_dragon)

#  Check if ‘on’ in both ‘python’ and ‘dragon’
print('on' in 'python' and 'on' in 'dragon')

# Check if ‘jargon’ in sentence
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

# Check if ‘on’ is not in both
print('on' not in 'dragon' and 'on' not in 'python')

# Convert length of text to float and string
length = len('python')
length_float = float(length)
length_str = str(length_float)
print(length_str)

# Check if a number is even
num = 4
is_even = num % 2 == 0
print("Is number even?", is_even)

# Floor division check
print(7 // 3 == int(2.7))

# Type comparison
print(type('10') == type(10))

# Convert ‘9.8’ to int
print(int(float('9.8')) == 10)

# Calculate weekly pay
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print("Your weekly earning is", pay)

# Calculate seconds lived
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# Display table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)