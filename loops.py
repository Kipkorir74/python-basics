#Loops control the flow of the code

# items = [1,2,3,4,5, "Hi"]
# for item in (items):

#     print(f"Round: {item}")


# items = " Pythonn"
# for item in (items):

#     print(f"Round: {item}")

# for item in range (1,10,2): #define the start, stop, step 
#     print(f"Round: {item}")


# scores = [80,90,60,75]
# total = 0 #Inititalize score to zero

# for score in scores:
#     total += score #Iterate through list, adding the values to the total for each iteration
# print ("Final Total:", total) 

# files = ['     Report.csv  ', '  DATA.csv ', ' final.txt'] #List with inconsictent casing and unnecessary spaces

# for file in files:
#     file = file.strip().lower().replace('.txt', '.csv')

#     print(f'Processing {file}' )

# Challenge PRINT THE 7 TIMES TABLE FROM 1 TO 10 USING A FOR LOOP
# for item in range(1, 11):
#     item *= 7 
#     print (f"7 x {item} =", item)

# Challenge 2 - Print a left aligned pyramid of stars with 6 rows using a for loop
# Set the number of rows
# rows = 6

# # Outer loop controls the rows which will run 6 times
# for item in range(1, rows + 1):
#     # Inner loop controls the stars printed in each row
#     for j in range(item): #When item is equals to 1 print 1 star, if 2 print 2 stars and so on
#         print("*", end="") # End ensure that the computer is printing stars on the same line instead of dropping down right away
#     # Move to the next line after finishing the row
#     print()


# names = ['John', 'Maria', '','Johnte']

# for name in names: #Loop through the names in the list
#     if name == '': #Once we reach an empty value, stop the loop
#         # print("Empty value detected!")
#         # break #stops loop immediately
#         # continue #skips the loop cycle based on condition and jump back to the loop
#         # pass #todo: Handle empty value
#         name = name.replace('', 'Kiboko')
#     print(f"Name = {name}")


#Task 1 - Loop through a list of days and print only the working days, skipping the weekends

# days = ['Mon', 'Teu', 'Wed', 'Sun', 'Thur']
# weekends = ['Sun', 'Sat']

# for day in days:
#     if day in weekends:
#         # print("Not a Working day")
#         continue
#     print(f"Workday: {day}")


# Task 2 - Scan emails to block unsafe data from entering system

# emails = [
#     'kiboko@gmail.com',
#     'mbuemoburesana@hotmail.com',
#     'DELETE INFO;',
#     'whyohwhydalot@outlook.com'
# ]

# for email in emails:
#     if ";" in email:
#         print("Email Error!")
#         break
#     print(f"Processing Email: {email}")

# items =[1,3,5,9]

# for item in items:
#     if  item % 2 == 0:  
#         print(f"Even Number found:{item}")
#         break
# else:
#     print("All numbers are odd") #Statement executed if python manages to iterate trjough the complete list
    

# # Task -Check for missing names in a list 
# names = ['Kamau', 'Kiprono', 'Mwenda', 'Onjiko', None, 'Omollo']

# for name in names:
#     if name is None:
#         print("Found Missing Name")
#         break
# else:
#     print("All Names Available")

#Task - Check if all files are csv files

# files = ['jobs.csv', 'jumbo.txt', 'tasks.csv', 'open.csv']

# for file in files:
#     if not file.endswith('.csv'):
#         print(f'Found a file that does not end with .csv: {file}')
#         break
# else:
#     print("All files end with .csv")

# # Challenge - Check whetehr we have any filename that appears more than once 
# file_list = ['data.xlsx', 'report.csv', 'summary.docx','report.csv','data.csv']
# seen = set() # Used to create an empty set or to convert other collections (like lists, tuples, or strings) into sets to automatically strip away duplicate values
# for item in file_list:
#     if item in seen:
#         print(f"Duplicate found, {item}")
#         break
#     seen.add(item)
# else:
#     print("All files are unique")

#Nested for loops

# for x in range (3):
#     for y in range(2):
#         print(f"({x}, {y})")

# colors = ['red', 'green','blue']
# sizes = ['L', 'M', 'S']

# for color in colors:
#     for size in sizes:
#         print(f'{color} - Size {size}')


# years = [2026,2027]
# months = ['Jan', 'Feb']
# days = range(1,29)

# for year in years:
#     for month in months:
#         for day in days:
#             print(f'report_{year}_{month}_{day}.csv')



# tables = ['customers','orders','products','prices']
# columns = ['ids', 'create_date']

# for table in tables:
#     for column in columns:
#         print(f'Select count(*) From {table} WHERE {column} IS NULL;')
#         continue

#While loop
# Build a counter from 1 to 5
# i = 1
# while i<=5:
#     print(i)
#     i+=1

# answer = ''

# while answer != "yes":
#     answer = input("Do you agree (yes/no):")
#     # answer.strip().lower()
# print("Thank You ")

# Challenge - limit user to three attempts,  

attempts = 0

while attempts < 3:
    answer = answer = input("Do you agree (yes/no):")
    if answer =='yes':
        print("Glad we are on the same page")
        break
    attempts+=1
else:
        print('Three strikes, You are out!')
 