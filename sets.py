my_set = {10,30,20,10}

# print(my_set) #unordered , no duplicates allowed

# print(my_set[2]) #not indexed

# my_set.remove(10) 
# print(my_set)

a = {10,20,30,40}

# a.add(25)
# print(a)

# a.update([1,2])
# a |={1,2} # alternative way of updating sets withouth using the update fn
# print(a)

# a.remove(20) #Unsafe way as it can break code if value to be removed not present
# print(a)

#Use discard instead. Removes item if exists, does nothing if it doesnt
# a.discard(11)
# print(a)

#mathematical operations
a = {12,14,33,67}
b = {14,22,56,33}

# merge 2 sets using union() fn. Unique values though
# print(a.union(b))
# print(a|b) # Alternative way use pipe

#Return shared values
# print(a.intersection(b) )
# print (a & b) #Alternative way 

# values in one list absent in the other 
# print(a.difference(b))
# print(a-b) #Alternative way 
# print(b-a)

# print everything not shared by the two sets
# print(a.symmetric_difference(b))


# relationship methods
# check if a ll items in are in b
print(a.issubset(b))

#check if b contains all values in a
print(b.issuperset(a))

#Check if two sets share same items. zero values in common
print(a.isdisjoint(b))