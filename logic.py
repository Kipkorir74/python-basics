email=''
phone = 1234567890
username = "user123"

# Validation
# print(any([email, phone, username])) # Output: True. Checks if at least one of the variables is non-empty (truthy).

# print(all([email, phone, username])) # Output: False. Checks if all of the variables are non-empty (truthy).

# print(isinstance(phone, str))  # Output: True. Checks if phone_number is an instance of the str class.

# print("Hello".endswith("o"))  # Output: True. Checks if the string ends with the specified suffix.

# # Operators

# print(5 > 3)  # Output: True. Greater than operator.
# print(5 < 3)  # Output: False. Less than operator.
# print(10==10)  # Output: True. Equality operator.
# print(10!=5)  # Output: True. Not equal operator.3


# x = 9

# print(x > 3 and x < 10)  # Output: True. Logical AND operator.
# print(x < 3 and x < 10)  # Output: False. Logical AND operator.
# print(x < 3 or x > 10)  # Output: False. Logical OR operator. 
# print(x > 3 or x > 10)  # Output: True. Logical OR operator. 

#Check if system is under pressure
# cpu_usage = 75
# memory_usage = 80

# print(cpu_usage > 70 or memory_usage > 95)  # Output: True. Checks if both CPU and memory usage are above the threshold.

# Check user credentials before logging in
# email = True
# password = False

# print (email and password)  # Output: False. Checks if both email and password are provided (truthy) before allowing login.

# print(not email)  # Output: False. Logical NOT operator. Inverts the truth value of email.

# Control Mixed conditions

# is_logged_in = False
# is_guest = False
# is_banned = True

# print(is_logged_in or is_guest and not is_banned)  # Output: True. Checks if the user is either logged in or a guest, and not banned. 

# # in operator - Checks if a value exists in a sequence (like a string, list, or tuple).
# print("date" in username)  # Output: True. Checks if the substring "user" is present in the username.

# # security check: esnsuring domain is not banned
# domain = "gooddomain.com"
# banned_domains = ["baddomain.com", "malicious.com", "spamdomain.org"]


# print(domain not in banned_domains)  # Output: False. Checks if the domain is not in the list of banned domains, ensuring it's safe to use.

# x = ['q', 'w', 'e', 'r', 't',]
# y = ['q', 'w', 'e', 'r', 't', 'y']

# print (x is y)  # Output: False. Checks if x and y refer to the same object in memory (identity comparison).
# print (x == y)  # Output: True. Checks if x and y have the same content (value comparison).

# Make sure an email exists and is valid before sending a notification
# email = ""

# print(email is not None and email!="")  # Output: False. Checks if email is not None and contains an "@" symbol, ensuring it's valid before sending a notification.

# Challenge 1 - Check if user's name is not empty and the age is greater than or equal to 18
# username = input("Enter Your Name:")
# age = int(input("Enter Your age: "))
# print(f"Your name is {username} and age is {age}")
# print (username is not None  and username  !="" and age >=18)

# # Challenge 2 - Check if password is at least 8 characters and does not have any spaces
# password = "butwqfdagsddsjiad"

# number_of_spaces = len(password) - len(password.strip())

# print(len(password) >= 8 and number_of_spaces == 0)

# Challenge 3 - Check if user's email is not empty, containes '@' and end with '.com'

# email = "kibokohatari@gmail.com"
# print(email !="" and '@' in email and email.endswith(".com"))

# # Challenge 4 = Check if username is a string, is not None, and is longer than 5 characters
# username = "Kapitani"

# print(type(username) is str and username is not None and len(username)> 5 )

# Challenge 5 = Check if user is either an Admin or a moderator, and either they are not banned or they've verified their email
# user_admin = True
# is_moderator = False
# is_banned = False
# is_verified = True

# print((user_admin or is_moderator) and (is_banned or is_verified))