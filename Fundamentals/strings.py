
# Types - Data Types
# name="Kip"
# type_of_name=type(name)
# print(type_of_name)

# age: int ="28"
# type_of_age=type(age)
# print(type_of_age)
# print("Your Age is:" + str(age))
# Win = False
# print(type(Win))

# Math
# password ="12ed8"
# print("The length of the password is:", len(password))

# if len (password) < 8:
#     print("Password is too short")

# text = """
#     python is a high-level, interpreted programming language that 
#     is widely used for web development, data analysis, artificial 
#     intelligence, scientific computing, and more. 
#     It was created by Guido van Rossum and first released in 1991. 
#     Python emphasizes code readability and simplicity, 
#     making it an excellent choice for beginners and experienced developers alike.
# """
# print(text.count("Python"))

# Transformations
# price = "$123,7889"
# print(price.replace(",", "").replace("$", "")) 

# phone_number = "+49 (123) 456-7890"
# print(phone_number.replace("+", "00").replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

# first_name = "John"
# last_name = "Doe"

# full_name = first_name + " " + last_name
# print(full_name)  # Output: John Doe

# folder_name = "C:/Documents/Projects"
# file_name = "report.txt"
# file_path = folder_name + "/" + file_name
# print(file_path)  # Output: C:/Documents/Projects/report.txt

# name = "Alice"
# age = 30
# is_student = True

# print(f"My name is {name}, I am {age} years old, and it is {is_student} that I am a student.")
# print("Heloo "+ name )


# # stamp ="2026-09-24"
# # print(stamp.split("-"))

# csv_data = "John,Doe,30,New York"
# print(csv_data.split(","))  # Output: ['John', 'Doe', '30', 'New York']

# Transformations
# print("*"*30) 

# # Indexing and Slicing
# text ="Python"

# # # Extract first character
# print(text[-4])  # Output: P
# print(text[2])   # Output: P

# date = "2023-09-24"
# # Extract year, month, and day using slicing
# print(date[1:4])  # Output: 2023 (year)
# # print(date[5:7])  # Output: 09 (month)
# # print(date[-2:]) # Output: 24 (day)
# print(date[::2])  # Output: 22-92 (every second character) start:stop:step


# # Removing Spaces
# text="  Engineer  "
# # print(text.strip("e"))  # Output: Engineer
# print(text.lstrip()) # Output: Engineer  
# print(text.rstrip()) # Output:  Engineer

# text = "###Engineer####"

# print(text.strip("#"))  # Output: Engineer


# text = "Engineer"
# number_of_spaces = len(text) - len(text.strip())
# is_clean = len(text.strip()) == len(text)
# print("Number of spaces removed:", number_of_spaces)  # Output: Number of spaces removed
# print("Is the text clean (no leading/trailing spaces)?", is_clean)  # Output: Is the text clean (no leading/trailing spaces)? False

# Case Conversion
# text ="python PROGRAMMING"
# print(text.upper())  # Output: PYTHON PROGRAMMING
# print(text.lower())  # Output: python programming
# print(text.capitalize())  # Output: Python programming
# print(text.title())  # Output: Python Programming

# search = "programming ".upper().rstrip()
# data = " Programming".upper().lstrip()

# print(search == data)  # Output: False
# # print(search.lower() == data.lower())  # Output: True

# print(search.lower() == data.lower())  # Output: True

# Search - Validate file names in system
phone1 = "+49-123-456-7890"
# phone2 = "+1-987-654-3210"
# print(phone1.startswith("+49"))  # Output: True
print(phone1[::-3])
# 9134

# email = "graham@gamil.com"
# print(email.endswith("gmail.com"))  # Output: True

# file ="report.pdf"
# print(file.endswith(".pdf"))  # Output: True

# print("@" in email)  # Output: True

# url = "https://api.greensett.com/v1/users"
# print("/api" in url)  # Output: True

# phone1 = "+49-123-456-7890"
# phone2 = "+1-987-654-3210"
# print(phone1.startswith("+49"))  # Output: True

# print(phone1[phone1.find("-")+1:]) # Output: 123-456-7890

# Validation
# country = "Germany1"
# print(country.isalpha())  # Output: False. Check if the string contains only alphabetic characters (letters).

# phone_number = "123456-7890"
# print(phone_number.isnumeric())  # Output: False. Check if the string contains only numeric characters (digits).
 