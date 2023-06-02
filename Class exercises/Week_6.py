"""
Functions class exercises
----------------------
Note: Remember a function will only run once it has been called.

(Slide 36 of Week 5 & 6
"""

# Q1 - Square of numbers
def square(number):
    """Returns the square of a number."""
    return number ** 2

# Q2 - Maximum of two numbers
def max_num(num1, num2):
    """Returns the larger of two numbers."""
    return max(num1, num2)


# Q3 - Tax calculator
def calculate_tax(salary):
    """
    Returns the amount of tax based on the given salary.

    Tax brackets:
    - Income up to €20,000: 0% tax
    - Income from €20,001 to €50,000: 10% tax
    - Income from €50,001 to €100,000: 20% tax
    - Income above €100,000: 30% tax
    """
    if salary <= 20000:
        return 0
    elif salary <= 50000:
        return salary * 0.1
    elif salary <= 100000:
        return salary * 0.2
    else:
        return salary * 0.3


# Q4 - String reversing
def reverse_string(string):
    """Returns the reverse of a string."""
    return string[::-1]

# Q5 - Average of numbers
def find_average(numbers):
    """Returns the average of a list of numbers."""
    return sum(numbers) / len(numbers)

# Q6 - Customer info
def customer_information(customer_name, customer_id, purchase_id):
    """
    Processes customer information and returns the result.

    Parameters:
        customer_name (str): Name of the customer.
        customer_id (int): ID of the customer.
        purchase_id (int): ID of the purchase.

    Returns:
        str: Result of the operation on the input variables.
    """
    result = f"Processing customer: {customer_name}, ID: {customer_id}, Purchase ID: {purchase_id}"
    # Perform any desired operation on the input variables
    # ...
    return result
