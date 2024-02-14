#syntax
#print("")

print("JJTECH")
print("Towerbatch")

a = "Raphael"
print(a)
print(type(a))

name = "Oluwaseyi"
print(name)
print(type(name))
print(len(name))

print("1"+"5")
print(1+5)
b = 1+6
print(b)
c = "1"+"2"
print(c)
print(type(b))
print(type(c))

print(True)
print(False)
print(type(True))
print(10 > 1)
print(9 < 10)
print(-50 > 10)

# a,c,d are a variables with int value 1,2,3
# b is a variable with str value JJtech
a = 1
b = "JJtech"
c = 2
d = 3
print(a+c)
print("a"+"d")
print("a"+b)


# Operators
# Arithmetic Operators

print("a",a)
print(sum , a+c)
print("sum:",a+c)
print("sub:",d-1)
print("mul:",c*d)
print("div:",3/2)
print("floor division:", 3//2)
print("modular:",d%c)
print("power to:", d**c)

# Assignment Operators
e = 4
print(e)
f = a+e
print(f)
a+=f # (its the same as a = a+f)
print(a)

# Comaparision Operators
print(f>a) # greater than
print(a==d) # equals
print(a!=c) # not equals
print(a>=d) # greater than or equals
print(a<=c) # less than or equal to

# Logical Operators
# I want biryani and coke => means I want both of them
# I want biryani or coke => means I want either of them
# I want biryani not coke => means I want biryani only
# The logical operators only operate on 3 items and, or, not to give an output
a = 6
b = 8
print((a<b) and (b>10)) # this output was False because the statement was False and True. 
print((a<b) and (b<10)) # this output was True becuase the statement was True and True
print((a<b) or (b>10)) # this output was True because the statement was True or False. 
print(not False) # anything not true is false, and anything not false is true.

# Bitwise Operators
# This type of operators only deals with binary numbers only.
# &, |, ~, >>, <<, means and, or, not, right-shift, left-shift

# Special Operators
# is, is not
a = 10
b = 10
print(a is b)
print(a is not b)

a = [1,2,3,4,5]
for i in a:
    print(i)

for i in a:
    if i is 4:
        print("Oluwaseyi")    
    else:
        print(i)

# Type conversion
print(str(1)+"Tower") # this was you change the data type of 1 from integer to string since (NOTE: Integer + String won't work)
a = 5
print(str(a)+"Tower")

# Data Structures
# List of Variables
fruits = ["banana","orange","apple","grapes","waternelon"] # list of strings
prices = ["$20","$50","$100","$150"] # list of string
numbers = [1,2,3,4,5,6] # list of numbers
my_list = ["banana",True, 1, 10.50] # list of values of variables that contains various data types from strings, boolean, numbers, floats

# printing the lists of items
print('n\# printing the list items')

print(fruits)
print(prices)
print(type(my_list))
print(type(numbers))
print(len(my_list))

fruits = ["banana","orange","apple","grapes","watermelon",[1,2,3,4,5,6] ] # nested list

print(fruits[0])
print(fruits[-1])

# slicing lists
print(fruits[1:3])

# how to update an existing new value
fruits[1]="pineapple"
print(fruits)

# to add a value to the existing list
fruits.append("fredy")
print(fruits)

# to update a list and insert the value into a specific place
fruits.insert(3,"Davis")
print(fruits)

# to remove a value from the list
fruits.remove("Davis")
print(fruits)

# to remove a value from the nested list
for i in fruits:
    if str(type(i)) == "<class 'list'>":
        print(i.remove(1))

print(fruits)

# Dictionary
cars = {"bently": 100,
        "lambogini": 200,
        "Toyota": 500,
        "honda": 600}

print(cars)
print(cars.get("bently"))
print(cars.keys())
print(cars.values())

if "bently" in cars:
    print("hello")
else: 
    print("bye")

# to update in this values or make a change to an existing value
cars['bently'] = 50  
print(cars)

# to show a loop  all the keys, all the values, and the items
for i in cars.keys():
    print(i)

for i in cars.values():
    print(i)

for i,y in cars.items():
    print(i,y)

# to clear all the items in cars variable
#cars.clear()
#print(cars)

# to make it give you a particular value
for harris, jannet in cars.items():
    if harris == "Toyota":
        print(jannet)

# Tuples, it cannot be changed or modified to differentiate tuple from list, tuple uses (), while list uses []
names = ('seyi', 'vamsi', 'avinash', 'showmilk')
print(type(names))       

#Set, to use this make use of curly brackets {}
list = {1,4,1,3,2,5}
print(list)


# Conditional Statement. This makes use of if condition, else condition, elif condition
marks = 60
if marks >= 90:
    print("A Grade")
else:
    print("C Grade")

# how to use the elif condition, this is a condition used to print other statements that may be met if the if and else
# is not true
# 20 - 30 ---> Great looking lady
# 30 - 40 ---> Average looking lady
# 50 ---> Any

age = 20
if age >= 40:
    print("Any")  

elif age >= 20:
    print("Great looking lady")

elif age >= 30:
    print("Average looking lady")

else:
    print("Nothing")    

#LOOPS, it usually have an iterator (i) and value
a = [1,2,3,4,5]
for i in a:
    print(i)    

for i in a:
    print("JJTECH")
    print(i)    

# manually defining the variable
b = 10    
for i in range(b):
    print(i)   

# for automatic process of looping
for i in range(20):
    print (i)         

team = ["petrollena", "fred", "bernard"]
for y in team:
    if y =="fred":
        print(y)
        print("jjtech")    

for y in team:
    if y =="fred" or y == "bernard":
        print(y)
        print("jjtech")  

# to skip printing petrollena
for y in team:
    if y == "petrollena":
        pass
    else:
        print(y)

# using the while loop: this type of loop reads continously until the defined conditions changes. 
# synthax:
# while expression:
    # statement
i = 0
while (i<=5):
    print('hello')
    i = i+1        

# nested loops
for i in range(5):
    for j in range(3):
        print("Tower")
    print("Hello World") 

# how to use the break and continue in the loop function
for i in range(10):
    if i == 5:
       break
    print("main loop", "value of i is:",i)    

for i in range(10):
    if i == 5:
       continue
    print("main loop", "value of i is:",i)


#### FUNCTIONS ###
def addition (a,b):
    print(a+b)
addition(5,7)        

def addition (a,b):
    print(a+b)
    print("Hello Team")

addition(5,7)
addition(10,15)
addition(20,30)

## Real life scenerio for creation of resources using boto3 and python using functions
#import boto3
#def createec2(amiid,instancetype,region):
#    client = boto3.client('ec2',region_name = region)
#    response = client.run_instance(

#        ImageId = amiid,
#        InstanceType = instancetype,
#        MaxCount = 1,
#        MinCount = 1
#    )
#createec2("provide ami id here", "provide instance type here", "provide your region here")

