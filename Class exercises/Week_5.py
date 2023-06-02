
"""
Conditional statements class exercises
----------------------
Discussion exercise (Slide 15 of Week 5 & 6)
"""

def thermostat_regulator(temperature, low_temp=  20, high_temp = 27):
    """
    A simple thermostat regulator function, creating an output state depending on an input temperature
    """
    if temperature < low_temp:
        state_thermostat = "Turn on heater"
    elif temperature > high_temp:
        state_thermostat = "Turn on cooler"
    else:
        state_thermostat = 'Do nothing'
    return state_thermostat


temperature = 25
state = thermostat_regulator(temperature)
print(state)


"""
Conditional statements class exercises
----------------------
(Slide 17 of Week 5 & 6)
"""

# Q1 Check the username
name = input("Enter your name: ")

if name == "James Bond":
    print("We've been expecting you, Mr Bond.")
else:
    print("Access Denied: " + name)

# Q2 Check the data type and return decimal
value = input("Enter a value: ")

try:
    value = float(value)
    if value.is_integer():
        print("Value is an integer.")
    else:
        decimal_component = value % 1
        print("Decimal component:", decimal_component)
except ValueError:
    print("Value is not a valid number.")

# Q3 Weekend plans based on factors
weather = input("Enter the weather condition: ")
season = input("Enter the season: ")

if weather == "sunny":
    print("Go outside.")
    if season == "summer":
        print("Play basketball.")
    else:
        print("Do something else.")
else:
    print("Stay indoors.")


"""
Looping class exercises
----------------------
(Slide 23 of Week 5 & 6
"""

# Q1 Congratulations message
names = ["Tom", "Alice", "Bob", "Emma", "John", "Lily", "Sam"]

for name in names:
    print("Congratulations", name + "!")

# Q2 Loop to print every letter in a string
string_example = "Hello, World!"

for letter in string_example:
    print(letter)

# Q3 Loop to append squares of numbers to a new list
lst1 = [3, 7, 6, 8, 9, 11, 15, 25]
lst2 = []

for num in lst1:
    lst2.append(num ** 2)

print(lst2)

# Q4 Loop to append squares of numbers to a new list catching strings
lst1 = [3, 7, 6, 8, 9, "11", 15, 25]
lst2 = []

for num in lst1:
    if isinstance(num, str):
        print("Index [{}] was a string, not an integer".format(lst1.index(num)))
        continue
    lst2.append(num ** 2)

print(lst2)

"""
While-loops exercises
----------------------
(Slide 28 of Week 5 & 6
"""

# Q1 - Number counter

counter = 0
total = 0

while counter <= 100:
    total += counter
    counter += 1

print(total)

# Q2 - Name iterator

names = ["John", "Bond", "Alice", "Bond", "Bob"]

index = 0
while index < len(names):
    if names[index] == "Bond":
        print("We've been expecting you, Mr Bond")
    index += 1