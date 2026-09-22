import math


# # built-in fns
# print(len("Python"))

# # fn from libraries
# number = 21.88327
# print(math.ceil(number))

# # user defined
# def morning_routine():
#     print("Wake up")
#     print("Gym")
#     print("breakfast")
#     print("shower")
#     print("work")

# morning_routine()

# Simple fn
# case_rule = 'upper' #gloabal variable 

# def clean_name(name):  
#     cleaned = name.strip() #Loacl variable
#     if case_rule =='upper':
#         cleaned = cleaned.upper()
#     print(cleaned)
# clean_name("Kiboko  ")
# clean_name("umaeR  ")

# def clean_name(first_name, last_name, country="NA"):  
#     first = first_name.strip().lower() #Loacl variable
#     last = last_name.strip().lower()
#     full_name = first + ' '+ last 
#     print(full_name + " from "+ country)
# clean_name("Kiboko  ", ' Yao') # Positional arguments
# clean_name(first_name="umaeR  ", last_name= "Dr ") #Keyword argument

# def total(*args):
#     print(sum(args))
# total(1,2)
# total(1,2,3)

# def create_user(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# create_user(name="Salah", age=34, country="Egypt")
# create_user(name="Messi", country="Argentina")


# # Return Keyword
# def clean_name(name): 
#     # if not name:
#     #     return None 
#     # else:
#     low_cleaned = name.strip().lower()
#     up_cleaned = name.strip().upper()
#     return low_cleaned, up_cleaned

# low_name,upp_name = clean_name(' Dante  ')
# print(low_name)
# print(upp_name)

# Task - store application log messages in a file whenenver an event occurs
 #  action fn - perfoms an operationn in the system instead of returning values

def write_log(message):
    with open(r"C:\Users\Public\Documents\app.log", "a") as file:
        file.write(message + '\n')
# write_log("App Started")
# write_log("User Logged in")
# write_log("App Stopped")

# transformation fns - raw data goes in, gets transformed and returns processed data 
#  Task - clean email addresses and splits them into structured data
def clean_and_split(email):
    clean_email = email.strip().lower()
    username, domain = clean_email.split("@")
    return {"Username": username,
            "Domain": domain}
# print(clean_and_split("  jjkipkip@gmail.com    "))

# Validation function - validates a condition and returns a boolean result
# Task Checks whether pwd meets minimum lenght of 8 characters
# def is_valid_password(password):
#    return len(password) >= 8

# print(is_valid_password("12345"))
# print(is_valid_password("12345qwqwqs"))

#Check if email address has a basic valid format 
def is_email_valid(email):
   return "@"in email and "." in email 
# print(is_email_valid("amanigmail.com"))
# print(is_email_valid("amani@gmailcom"))
# print(is_email_valid("amani@gmail.com"))

# orchestrator fn - controls program flow, calls other fns in correct order
# def process_user_email(email):
#     write_log("Application Started")

#     #validate the email 
#     #if not valid log an error i a file
#     if not is_email_valid(email):
#         write_log(f"Invalid email received: {email}")

#     # if valid clean and structure the email
#     else:
#         clean_email = clean_and_split(email)
#         write_log(f"Processed email: {clean_email}")
#     # log each step of the program 
#     write_log("Application ended")

# # project Receive email from user
# email = input("Please enter your email:")
# process_user_email(email)

def calculate_discount(price: float,rate: float) -> float:
    """
    Calculate the final price after applying the discount
    Args:
        price(float): Original Product Price
        rate (float): Discount rate as numbers (eg 20 for 20%)
    Retuns:
        final_price(float) Final price after applying discount
    """
    final_price = price -(price * rate / 100)
    return final_price
print(calculate_discount(100,20))