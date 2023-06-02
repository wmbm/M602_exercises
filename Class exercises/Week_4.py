"""
Data types class exercises
----------------------
(Slide 24 of Week 3 & 4)
"""

# Q1
value_string = input("Please write an input string")
print(len(value_string))

# Q2
value_int_1 = input("Enter your first integer")
value_int_2 = input("Enter your second integer")
print("The sum of the two values is: ", value_int_1 + value_int_2)

"""
Data structures  class exercises
----------------------
Note: Q2 below uses "list comprehension" a topic we'll come back to in later lessons. 

(Slide 33 of Week 3 & 4)
"""

# Q1
example_list = [1, 5, 6, 7, 8]
print(max(example_list))
print(min(example_list))

# Q2
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Time', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_people = sorted(people, key=lambda x: x['age'])

sorted_names = [person['name'] for person in sorted_people]



