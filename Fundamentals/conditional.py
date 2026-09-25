# # If statement defines the condition
score = 8433545
project_Submitted = True
# if score >= 90 and project_Submitted: # Checks whether 2 conditons are met. the score and whether project was submitted print if true else proceed to second condition
#     print("A+")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 60:
#     print("C")
# elif score >=50 or project_Submitted:
#     print("D")
# else:
    # print("F")

# Independent if statements
# if score > 90:
#     print("High Score")
# else:
#     print("Low Score")

# if project_Submitted:
#     print("Project is submitted")
# else:
#     print("Project is not submitted")

# inline if statements - Used when logic is simple
# print("A" if score >= 90 else "F")

# grade = "A" if score >= 90 else "B" if score >= 80 else "F"
# print(grade)

# Match case -Evaluates a value against multiple values

# country = "England"

# if country =="United Kingdom":  #Flexible Logic and multiple conditions
#     print("UK")
# elif country =="India":
#     print("IN")
# elif country =="Kenya":
#     print("KE")
# elif country =="China":
#     print("CN")
# else:
#     print("Unknown Country")

# match country:    # Used only for matching velues. Easy to Read 
#     case "United Kingdom" | "England":
#         print("UK")
#     case "India":
#         print("IN")
#     case "Kenya":
#         print("KE")
#     case "China":
#         print("CN")
#     case _:   # Default
#         print("Unknown Country")

# Challenge #1
# Validate the quality and correctness of email values
# Must not be empty. must contain "." and "@" , must contain exatly one "@" symbol
# Must end with '.com','.org', or '.net' and Must not be longer than 254 characters
# Must start and end with a letter or digit

# email = "___citywataonamoto@@gmail.com "
# valid = True
# email = email.strip()

# valid_email = (".com", ".org", ".net" )

# if not email:
#     print("Email cannot be empty") 
#     valid = False
# if len(email) > 254:
#     print("Email is longer than the required Length")
#     valid = False
# if not ('@'in email and '.' in email):
#     print("Email msut contain @and .")
#     valid = False
# if email.count('@') != 1:
#     print("Email must have only one @ ")
#     valid = False
# if not email.endswith(valid_email):
#     print("Email must end with .com, .org, .net")
#     valid = False
# if not(email[0].isalnum() and email[-1].isalnum()):
#     print("Email must start and end with an alphabet or digit")
#     valid = False
# if valid:
#     print("This is a valid email")


#Challenge 2
# Validate the quality and correctness of passwords
# Must not be empty, must be atleast 8 characters, Must include at least one uppercase,
# must include one lowercase, msut not be the same as the email address, must not contain any spaces
# musts start and end with a letter or digit

# password = "Ysdfghkjlgfuey7g7w"
# email = "kiboko@gmail.com"
# valid = True
# number_of_spaces = len(password) - len(password.strip())

# if not password:
#     print("Password cannot be empty")
#     valid = False
# if len(password) < 8:
#     print("The Password cannot be less than 8 characters")
#     valid = False
# if not any(char.isupper() for char in password):
#     print("Password must include at least one uppercase")
#     valid = False
# if not any(char.islower() for char in password):
#     print("Password must include at least one lowercase")
#     valid = False
# if password == email:
#     print("Email Cannot be the same as the password")
#     valid = False
# if number_of_spaces != 0:
#     print("Password must not contain any spaces")
#     valid = False
# if not (password[0].isalnum() and password[-1].isalnum()):
#     print("Email must start and end with an alphabet or digit")
#     valid = False
# if valid:
#     print("The password is correct")
