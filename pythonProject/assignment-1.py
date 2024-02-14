# Create a list of your favorite movies and print it.
movies = ["adire","tarzan","lost city","home alone"]
print(movies)

# Append a new movie to the list and print the updated list.
movies.append("house of cards")
print(movies)

# Build a dictionary representing a car with keys like ‘brand’, ‘model’, and ‘year’.
car = {"brand": "honda",
        "model": "pilot",
        "year": "2015"} 

# Add a new key-value pair to the dictionary and print the updated dictionary.
car["owner"] = "oluwaseyi"
print(car)

# Create two sets of numbers and find their union and intersection.
numbers01 = {1,2,3,4,5,6}
numbers02 = {4,5,6,7,8,9}

# finding the union
union_result = numbers01.union(numbers02)
print("Union:", union_result)

# finding the intersection 
intersection_result = numbers01.intersection(numbers02)
print("Intersection:", intersection_result)

# Check if one set is a subset of another.
# question 1 is set number02 subset to number01
is_subset = numbers02.issubset(numbers01)

if is_subset:
    print("number02 is a subset of number01")
else:
    print("number02 is not a subset of number01")

# question 1 is set number01 subset to number02 
is_subset = numbers01.issubset(numbers02)

if is_subset:
    print("number01 is a subset of number02")
else:
    print("number01 is not a subset of number02") 

# Create a tuple of three elements and print each element.
carmodels = ("honda","toyota","nissan","lexus")
songgenre = ("afrobeats","pop","rap","reggae")
housetypes = ("bungalow","duplex","storeybuilding","townhome")

# Implement a program that checks if a number is positive, negative, or zero using if-elif-else.
age = 19
if age <= 20:
    print("Positive")  

elif age >= 40:
    print("Negative")

else:
    print("Zero")    

# Write a program to determine if a student’s grade falls into categories: ‘A’, ‘B’, ‘C’, ‘D’, ‘F’.
# 80 - 100 --> Grade A
# 70 - 79 ---> Grade B
# 60 - 69 ---> Grade C
# 50 - 59 ---> Grade D
# 40 - 49 ---> Grade F        

marks = 60
if marks <= 49:
    print("Grade F")  

elif marks <= 59:
    print("Grade D")

elif marks <= 69:
    print("Grade C")

elif marks <= 79:
    print("Grade B") 

else: 
    print("Grade A")   

# Using a list, check if a given item is present, and print a corresponding message.
holiday = ["barsoap", "haircream", "towels", "toothpaste", "toothbrush", "sponge"]

if "bodywash" in holiday:
    print("It is present")
else:
    print("It is not present")

def addition(a,b):
    return a+b

def subtration(c,d):
    return c-d

def multiplication(e,f):
    return e*f

value1 = addition(2,3)
print(value1)

value2 = subtration(10,7)
print(value2)

value3 = multiplication(4,5)
print(value3)

# file handling 
import os
#file_name = open(' /c/Users/oyase/OneDrive/Desktop/Cloud/project-folder/Repositories/pythonrepo/README.md', 'r')
#print(file_name.read())

file_path = '/c/Users/oyase/OneDrive/Desktop/Cloud/project-folder/Repositories/pythonrepo/README.md'

# Open the file using a context manager
with open(file_path, 'r') as file_name:
    print(file_name.read())
