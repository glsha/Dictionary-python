# Write The code to prompt a user to enter the following details:

# Name
# Email
# Number
# Address
# Use the values of entered to create a nested dictionary

# Hint: use dict.fromkeys()

 

# Expected Result:

#       {'john': {'email': 'john@gmail.com', 'number': 24020000000,  'address': ' 11901 Wornall Road, Kansas City, MO 64145'}}

name = input("Enter your name: ")
email = input("Enter your email: ")
number = input("Enter your number: ")
address = input("Enter your address: ")

user_details = {
    name: dict.fromkeys(['email', 'number', 'address'])
}

user_details[name]['email'] = email
user_details[name]['number'] = number
user_details[name]['address'] = address

print(user_details)