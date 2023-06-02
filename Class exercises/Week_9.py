"""
Strings class exercises
----------------------
(Slide 13 of Week 9)
"""

# Q1 - Counting characters
def count_occurrences(string, character):
    return string.count(character)

# Q2 - Checking substring presence
def check_substring_presence(string, substring):
    return substring in string

# Q3 - Changing case
def change_case(string):
    lower_case = string.lower()
    upper_case = string.upper()
    return lower_case, upper_case

# Q4 - Splitting and joining strings
def split_and_join(string, delimiter):
    words = string.split()
    joined_string = delimiter.join(words)
    return joined_string

# Removing whitespace
def remove_whitespace(string):
    return string.strip()


# Test the functions
input_string = "Hello, World! How are you today?"
character_count = count_occurrences(input_string, 'o')
print("Character count:", character_count)

substring_present = check_substring_presence(input_string, "are")
print("Substring present:", substring_present)

lowercase, uppercase = change_case(input_string)
print("Lowercase:", lowercase)
print("Uppercase:", uppercase)

delimiter = "-"
joined_string = split_and_join(input_string, delimiter)
print("Joined string:", joined_string)

whitespace_removed = remove_whitespace(input_string)
print("Whitespace removed:", whitespace_removed)

"""
Regular expressions class exercises
----------------------
(Slide 19 of Week 9)
"""

import re

# Q1 - Validating email addresses
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Q2 - Extracting phone numbers
def extract_phone_numbers(string):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    return re.findall(pattern, string)

# Validating URLs
def validate_url(url):
    pattern = r'^(http|https):\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}\b'
    return re.match(pattern, url) is not None

# Finding duplicate words
def find_duplicate_words(string):
    pattern = r'\b(\w+)\b(?=.*\b\1\b)'
    return re.findall(pattern, string)


# Test the functions
email = "example@example.com"
is_valid_email = validate_email(email)
print("Is valid email:", is_valid_email)

text = "Call me at 123-456-7890 or 987-654-3210 for assistance."
phone_numbers = extract_phone_numbers(text)
print("Phone numbers:", phone_numbers)

url = "http://www.example.com"
is_valid_url = validate_url(url)
print("Is valid URL:", is_valid_url)

text = "This is a test. This is only a test."
duplicate_words = find_duplicate_words(text)
print("Duplicate words:", duplicate_words)