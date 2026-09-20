user ={'id':1, 'age':30, 'city':'Kenya'}

# Access
# print (user.get('name', "Unknown")) #Retreive values safely

#Checks
# print('age' in user)

# view objects
# print(user.keys())
# print(user.values())
# print(user.items())

#Looping
# for u in user:
#     print(u, user[u])

# for key, value in user.items():
    # print(key,value)

# Add, Remove, Update
user["name"] = "John" #Adding values 

user["age"] = 28 #Updating existing values by referencing to existing key or add new values if key not existent
# print(user)

# user.update({"age":20, 'city':"Memphis"})
# print(user)

# age = user.pop("age","Not found")
# print(user)
# print("Removed Item:", age)

# user.popitem()
# print(user)


#Creation
# user = {
#     'id': None,
#     'name': None,
#     'age': None,
#     'city': None 
# }

# user.fromkeys(['id', 'name', 'age','city'], None) #Use this inititally when we don't know the values then update later
# print(user)

# Challenge
# create new dict, keep only pairs with string values, convert values to uppercase

user ={'id':1, 'name':'Johnte', 'age':30, 'city':'Kenya'}

new_dict ={
    # expression
    key.upper():value.upper()
    # Loop
    for key,value in user.items()
    # Filter
    if isinstance(value, str)
}
print(new_dict)
