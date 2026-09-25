#Creating Lists
# empty = []

# letters = ['a','b','c','d']
# numbers = [1,2,3,4]
# mixed = [1,'a', True, None]

# print(type(mixed))

# empty = list()
# print(empty)

# letters = list('Python') #Create list using built in fn list()
# print(letters)

# numbers = list(range(5)) 
# print(numbers)

# nested lists
# matrix = [['a','b','c'],
#           ['d','e','f']]
# mixed_matrix = [[1,2,3], ['a','b','c']]

# print(matrix)
# print(type(matrix))
# print(mixed_matrix)

# # accessing and reading lists
# lst = ['a','b','v','f','z','m']

# print(lst[-1]) #accessing items within the lists using indexes
# print(lst[::2])
# print(lst[2:])
# print(lst[1:3])
# print(lst)



# matrix = [
#     ['a','b','c'], #Row 0
#     ['d','e','f'], #Row 1
#     ['g','h','i']  #Row 2
# ]

# # print(matrix[1][1])
# # print(matrix[:2]) #Prints row 0 and 1
# # print(matrix[1:]) #Prints row 1 and 2
# print(matrix[1][:2]) #prints the first two items in row 2

# Unpacking lists
import copy


person = ['Kibe',42,'Streamer', 'Kenya', 'Humorous']
# name = person[0]
# age = person[1]
# career = person[2]
# country = person[3]

# name, age, career, country, trait = person
# # name, *details, country, _ = person #Use asterisk to retrieve only data you are intersteted in. Use only one 
# # name, _ , _ , country, _ = person #Use underscore to skip data not intersted. Can use multiple 
# name, *_, trait =person # Can use both asterisk and underscore
# print(name)
# # print(details)
# # print(age)
# # print(career)
# # print(country)
# print(trait)


numbers=[41,27,34,43,0,67,53,67]

# print("Max:", max(numbers))
# print("Min:", min(numbers))
# print("Sum:", sum(numbers))
# print("Length:", len(numbers))

# print("All:", all(numbers))
# print("All:", all([1,0,2]))
# print("All:", all(['a','b','c','']))

# print("Any:", any(numbers))
# print("Any:", any(['a','b','c','']))
# print("All:", any([0,0,0]))

# print("Count:", numbers.count(67))
# print("Index:", numbers.index(67)) #Returns the position of the first occurance of a value

# # Analysis and checks
# print(67 in numbers)
# print(67 not in numbers)

# list1 = [41,27,34,43, 67,53,67]
# list2 = [41,27,34,43, 67,53,67]

# print(list1==list2)
# print(list1 is list2) #Values identical but stored in separate lists in memory. Not pointing to same memory address

# Changing lists
# letters = ['a','b','c','d']
# # letters.append('e') #Append adds values at the end of the list
# # letters.append('f')
# # print(letters)

# letters.insert(2,'y') #Insert take in two parameters, first the position you want to inster and the value you want to insert

# print(letters)

matrix = [
    ['a','b','c'], #Row 0
    ['d','e','f'], #Row 1
    ['g','h','i']  #Row 2

]
# matrix.append(['j','k','l'])
# print(matrix)

# matrix.insert(0, ['m','n','o'])
# print(matrix)

# matrix[2].append('y')
# print(matrix)

# matrix[2].insert(1,'x')
# print(matrix)


letters = ['a','b','c','d', 'b']

# letters.clear() 
# print(letters)

# letters.remove('b')
# print(letters)

# removed = letters.pop(1)
# print(letters)
# print('Removed Item:',removed)
matrix = [
    ['a','b','c'], #Row 0
    ['d','e','f'], #Row 1
    ['g','h','i']  #Row 2
    ]

# matrix.remove(['a','b','c'])
# matrix.pop(1)
# matrix[1].remove('f') #Removes by defining the value
# matrix[1].pop(2)  #Removes by position
# print(matrix)

letters = ['a','b','c','d', 'b']

# letters[0]='r'
# letters[1]='s'
# letters[2]='t'
# letters[3]='u'
# letters[4]='v'
# print(letters)

# matrix[1][1]='j'

# print(matrix)

#Sorting 



# letters.sort(reverse=True)
# print(letters)

matrix = [
    ['a','b','c'], #Row 0
    ['g','h','i'],  #Row 2
    ['d','e','f'], #Row 1
    ['j','h','i']
]

# matrix.sort()
# matrix.sort(reverse=True)
# matrix[3].sort()
# print(matrix)
letters = ['c','a','b']

# new_list = sorted(letters)
# print('Original list:',letters)

# print("New List:",new_list)

# letters.reverse()
# new_list = list(reversed(letters)) #Creates a copy
# print('Original list:',letters)
# print('Reversed list:',new_list) #


 #Copying
letters = ['a','b','c','d', 'b']
# letters_copy = letters #Copying using assignment operator
# letters.append('z')
# letters.pop(2)

# print("Original letters: ", letters)
# print("Copy: ", letters_copy)
# print(letters)
letters_copy = letters.copy() #Creates a separate list in memory

letters_copy.append('i')


# print("Original letters: ", letters)
# print("Copy: ", letters_copy)

matrix = [
    ['a','b','c'], #Row 0
    ['g','h','i'],  #Row 1
]

# matrix_copy = copy.deepcopy(matrix) 
# # matrix_copy = copy.copy(matrix)
# # matrix.pop()
# matrix_copy[0].append('z')
# print("Original Matrix: ", matrix)
# print("Copy: ", matrix_copy)

original = [
    ['a','b'], #Row 0
    ['g','h'],  #Row 1
]

# # Assigment
copy1 = original  #Referencing to same object in mememory

# print("Same Object?", original is copy1) 

#Shallow copy
# copy2 = original.copy()
# print("Same Object?", original is copy2, '\n')
# print("Shared Lists?", original[0] is copy2[0] ) #Sharing same children but not same objects

# deep copy
# copy3 = copy.deepcopy(original)
# print("Same Object?", original is copy3, '\n')
# print("Shared Lists?", original[0] is copy3[0] ) #Sharing same children but not same objects

# Combining Lists
# letters = ['a','b','c']
# numbers = [1,2,3,4]

# comb = letters + numbers
# comb=[letters,numbers]
# numbers.extend(letters)
# comb = list(zip(letters,numbers))
# print(numbers)
# print(letters)
# print(comb)

# ids = [100,200,300]
# names=['John','Kipchoge', 'Martine']

# print(list(zip(ids,names)))

letters = ['a','b','c', 'd']
numbers = [1,2,3,4,5]
# # new=[]

# # for l in letters:
# #     new.append(l.upper()) #Store them in the new list
# #     print(new)

# #enumerate
# print(list(enumerate(letters, start = 2))) #takes in 2 params, can edefine where we start

# for index, value in enumerate(letters, start =2):
#     print(index,value) 

# for l in reversed(letters):
#     print(l)
# for n,l in zip(letters, numbers):
#     print(n,l)

# print(list(map(str.upper,letters)))

# numbers = ['1','2','3','4','5']
# print(list(map(int,numbers))) #connverts the string of numbers to integres

names = ['Johnte   ', '  Kiprono  ', '  Mwangi'] #Can be used to remove spaces in strings using strip found in the class string
# print(list(map(str.strip, names)))

# for n in map(str.strip, names):
#     print(n)

# letters = ['a','b','',None, 'c', False] 
# print(list(filter(bool, letters)))

# items=['sql','123','python', '42']

# # print(list(filter(str.isalpha,items)))

# for i in filter(str.isalpha,items): #Alternative. using fro loos
#     print (i)

# lambda

# multiply = lambda x: x*2
# print(multiply(3))  #multiply store a lambda function which doubles ythe number

# add = lambda x,y: x + y
# print (add(9,5)) #when lambda has 2 params, must pass two values when calling it

# check = lambda i: i in "kiboko"
# print(check("k"))

# prices=['$12.89','17.99','62.22'] #Transform the list from a list of strings to a list of floats

# # print(list(map(lambda p:float(p.replace('$','')), prices)))

# print(list(map(lambda p: float(p.replace("$",'')),prices)))


# p = "12.50" #Consider first replacing the $ with nothing to start with. Then apply the formula to the list
# print(float(p.replace('$',''))) #Formula to sort the above list, prices

# prices = [110,222,456,980]
# print(list(filter(lambda p: p >=200, prices)))
# print(list(filter(lambda p: p >= 300,prices)))

# students = [['Luka', 76],
#             ['Abunwasi',92],
#             ['Omondi', 65]    
#             ]
# print(list(filter(lambda row:row[1] > 70, students) )) #Reterive students with score higher than 2

# print(list(filter(lambda row: row[0].startswith('A'), students)))

# comprehension

# domains = ['www.google.com',
#            'jumanji.com',
#            'localhost',
#            'WWW.CARRICKBALL.COM'] #Normalize the domains into standard format

# cleaned = [
#     #Data transformation
#     d.upper().replace('www.','')
#     # loop
#     for d in domains
#     #data filtering
#     if '.' in d
# ]

# print (cleaned)