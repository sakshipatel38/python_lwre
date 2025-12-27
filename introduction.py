#what is python??

# dynamically typed language , general purpose programming language , supports object oriented programming , interpreted language
# created by guido van rossum in late 1980s and first released in 1991

# python is known for its simplicity and readability , making it a great choice for beginners and experienced developers alike
# it has a large standard library and a vast ecosystem of third-party packages , making it suitable for a wide range of applications , including web development , data analysis , artificial intelligence , scientific computing , automation , and more

#features of python ::

# 1. platform independent 
# 2. easy to learn and use
# 3. open source programming language
# 4. extensive standard and big library supports 
# 5. possible to integrate other programming language within python

# applications of python ::

# 1. web development ( django , flask )
# 2. data analysis and visualization ( pandas , matplotlib , seaborn )
# 3. machine learning and artificial intelligence ( tensorflow , scikit-learn , keras )
# 4. scientific computing ( numpy , scipy )
# 5. automation and scripting ( selenium , beautifulsoup )
# 6. game development ( pygame )
# 7. desktop application development ( tkinter , pyqt )
# 8. network programming ( socket , twisted )
# 9. cyber security ( scapy , nmap )
# 10. iot ( micro python , circuit python )
# 11. blockchain development ( web3.py , brownie )
# 12. cloud computing ( boto3 , google-cloud-python )
# 13. mobile app development ( kivy , beeWare )
# 14. robotics ( ROS , pybotics )
# 15. bioinformatics ( biopython )
# 16. education ( turtle , jupyter notebooks )
# 17. devops ( ansible , fabric )
# 18. augmented reality and virtual reality ( AR.py , Vizard )
# 19. natural language processing ( nltk , spaCy )
# 20. computer vision ( opencv , pillow )
# 21. database programming ( SQLAlchemy , peewee )
# 22. testing and debugging ( pytest , unittest )
# 23. geospatial analysis ( geopandas , shapely )
# 24. audio and music processing ( pydub , librosa )

# overall , python's versatility and ease of use have made it one of the most popular programming languages in the world today

'''IN PYTHON EVERYTHING IS AN OBJECT'''

# modules in python ::

# 1 >> PIP : 

'''pip is a python package manager that allows you to install and manage third-party packages and libraries'''

'''It is Pythons package manager, meaning:
pip stands for “Pip Installs Packages”
It downloads Python libraries from the internet (PyPI - Python Package Index)
It installs them into your Python environment
It can also update or remove libraries
Think of pip like an app store for Python libraries.'''

# 2 >> pandas : 

'''pandas is a very popular Python library used for:

Working with tables (rows & columns)
Data analysis
Reading CSV, Excel, SQL files
Cleaning and transforming data
It is widely used in data science, analytics, and machine learning.'''


# What are dependencies?

'''
Dependencies are other libraries (packages) that a program or library needs in order to work properly.
👉 In simple words:
A dependency is something your software depends on.

Simple real-life example 

Imagine you want to bake a cake.

To make the cake, you need:
    Flour
    Sugar
    Eggs
    Oven

These are dependencies of the cake.
Without them, the cake cannot be made.

Programming example (pandas)

When you install pandas, it does not work alone.

It depends on other libraries such as:

    numpy → fast math & array operations
    python-dateutil → date & time handling
    pytz → time zones
So:

pandas
 ├── numpy
 ├── python-dateutil
 └── pytz
 
These are pandas’ dependencies.

What happens when you run:
pip install pandas
    pip automatically:
    Installs pandas
    Checks what pandas depends on
    Downloads & installs all required dependencies
'''
# 3 >> scikit-learn :

'''Scikit-learn is an open-source machine learning library built on top of NumPy, SciPy, and Matplotlib. It provides easy-to-use tools for data analysis and predictive modeling.

Key Features ::

-->Simple & consistent API – easy to learn and use
-->Efficient performance for medium to large datasets
-->Well-documented with many examples
-->Integrates smoothly with other Python libraries

Main Functionalities
1. Supervised Learning
2. Unsupervised Learning
3. Model Selection & Evaluation
4. Data Preprocessing
'''

# repl : read , evaluate , print , loop --> it is format of cmd programming

# built-in module in python :: That modules are stored in the python package already  itself
# external module in python :: those modules are installed by user using pip command  

#first python program ::

'''print function is used to display output on the screen'''

# line by line excecution of code

# output : Hello, World!
# print("Hello, World!")

'''comments : In python comments are used to explain the code and make it more readable'''

'''escape sequences : special characters that are used to represent certain characters in a string and they are preceded by a backslash '''

# print("hello world \nwelcome to python programming")

print("hello ", 6 , 7 , sep='-' , end = '009\n')

# here "sep" is used to put sign between the values while printing them and connnect the outputs. 
# here space is default separator between values while printing them.

# here "end" is used to put specific value at the end of the print statement instead of new line.


'''variable and Data types in python'''
# variable is stored in RAM memory of computer.

a = 5 
b= 6.7
c = "hello"
d = 'h'
e = True
f = None
g = 3+4j
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g))

# type() : type() function is used to know the data type of variable or value.
# integer , float , string , character , boolean , NoneType , complex number are the data types in python.
# this is already a built in data types in python. we dont have to declare data types in python. python automatically detects the data type of variable while assigning value to it.


'''sequence data-types in python'''

#list 

list1 = [a , b , 1 , 2, 3.4 , "harry"] 
# list is a sequence data-type and is mutable (can be changed) and stored different types of data.
print(list1)
print(type(list1))

#dictionary 

disc1 = { "name" : "harry"} 
# mapped data , key value pair format , mutable (can be changed)
print(disc1)
print(type(disc1))

#tuple

tuple1 = (a , b , 1 , 2, 3.4 , "harry") 
# tuple is a sequence data-type and is immutable (cannot be changed) and stored different types of data.
print(tuple1)
print(type(tuple1))

#set 

set1 = {a , b , 1 , 2, 3.4 , "harry"} 
#  mutable (can be changed) and stored different types of data. it does not allow duplicate values.
print(set1) 
print(type(set1))


# OPERATORS IN PYTHON ::

'''arithmetic operators : + , - , * , / , %(modulus) , //(floor division) , ** (power) , *** (exponent)'''
'''++ , --  (not available in python) '''


#type casting in python : type-casting means converting one data-type to another data-type as much as it can try.

'''types of type-casting : 1.implicit type-casting
                           2.explicit type-casting'''

# implicit type-casting : it is done by python interpreter automatically when we perform operations on mixed data-types.
# explicit type-casting : it is done by programmer manually by using built-in functions like int() , float() , str() etc.

a = "10"
b = "20"
c = a+b
print("the value of c is :" , c)

# reason of above output is that a and b are string data-type so when we use + operator it concatenates the two strings.

a = "10"
b = "20"
c = int(a)+int(b)
print("the value of c is :" , c)

# here we have type casted the string before addition so the output is 30.

# during type casting it will convert lower odrer data-type to higher order data-type. e.g int to float , float to complex etc.

a = 5.6
b = 3   
c = a + b 
print("the value of c is :" , c)
print(type(c))
# here int b is converted to float before addition so the output is 8.6

a = 5.6
b = 3 + 4j  
c = a + b 
print("the value of c is :" , c)
print(type(c))

# here float a is converted to complex before addition so the output is (8.6+4j)

#user input function in python :: use for taking input from user during program execution.

a = input("enter your name : ")
print("your name is : " , a) 

# without type casting input function takes input as string by default.
# input type casting 

b = int(input("enter your age : "))
print("your age is : " , b)

# here we have type casted the input to int so the output will be integer.

c = float(input("enter your excat salary : "))
print("your excat salary is : " , c)

# here we have type casted the input to float so the output will be float.


'''STRINGS CHAPTER'''


#string in python : strings are used when working with unicode charachters and text data.
str1 = "hello world"
print(type(str1), str1, sep="-")

# st2 = '''Scikit-learn is an open-source machine learning library built on top of NumPy, SciPy, and Matplotlib. It provides easy-to-use tools for data analysis and predictive modeling.

# Key Features ::

# -->Simple & consistent API – easy to learn and use
# -->Efficient performance for medium to large datasets
# -->Well-documented with many examples
# -->Integrates smoothly with other Python libraries

# Main Functionalities
# 1. Supervised Learning
# 2. Unsupervised Learning
# 3. Model Selection & Evaluation
# 4. Data Preprocessing
# '''

# print(st2)
print(str1[0])
print(str1[6])#space is also a character and consider while counting index
'''print(str1[11])#through a error as index out of range'''

'''string slicing:'''

name  = "0abcdefghijkl"
print(len(name))#len() function is used to find the length of string 
print(name[0])#o/p : 0
print(name[0:5])#o/p : 0abcd
print(name[:5])#o/p : 0abcd bcz python by default take starting index as 0
print(name[5:])#o/p : efghijkl bcz python by default take ending index as length of string
print(name[:])#o/p : 0abcdefghijkl bcz python by default take starting index as 0 and ending index as length of string
print(name[-1])#o/p : l bcz -1 index represent last character of string but it doesn't print reverse string 
print(name[-4:-1])#o/p logic it is simply  "lenght of string - given negative index" here 13-4 = 9 means i 

for i in name:
    print(i , sep= " ", end = " ,") 


'''string of methods'''

#string are immutable means we cannot change the characters of string by using indexing. but you can reassig the string variable to new string.
str2 = "hello world\n"
print(str2.upper())# upper() method is used to convert all characters of string to uppercase and it copy the old string to new temporary string

print(str2.lower())# lower() method is used to convert all characters of string to lowercase

print(str2.replace("world" , "python"))# replace() method is used to replace a substring with another substring in string

print(str2.rstrip("d"))# it removes the specified character from right end of string

print(str2.lstrip("h"))# it removes the specified character from left end of string

print(str2.split(" "))# split() method is used to split the string into list of substrings based on specified space given in the argument

print(str2.capitalize())# capitalize() method is used to convert first character of string to uppercase and rest to lowercase

print(str2.center(20 , "*"))# center() method is used to center the string in a field of given width and fill the remaining space with specified character

print(str2.count("l"))# count() method is used to count the number of occurrences of a substring in string

print(str2.endswith("o"))# endswith() method is used to check if the string ends with specified substring or not and return boolean value 

print(str2.find("o"))# find() method is used to find the index of first occurrence of a substring in string and return -1 if not found

print(str2.index("l"))# index() method is used to find the index of first if it dosen't find it throws an error

print(str2.isalnum())# isalnum() method is used to check if all characters in string are alphanumeric or not and return boolean value 


# alphanumeric (a-z , A-Z , 0-9) 

print(str2.isalpha())# isalpha() method is used to check if all characters in string are alphabetic or not and return boolean value

# alphabetic (a-z , A-Z)

print(str2.islower())# islower() method is used to check if all characters in string are lowercase or not and return boolean value

print(str2.isprintable())# isprintable() method is used to check if all characters in string are printable or not and return boolean value

print(str2.isspace())# isspace() method is used to check if all characters in string are whitespace or not and return boolean value

print(str2.istitle())# istitle() method is used to check if string is in title case or not and return boolean value

print(str2.isupper())# isupper() method is used to check if all characters in string are uppercase or not and return boolean value

print(str2.swapcase())# swapcase() method is used to convert uppercase characters to lowercase and lowercase characters to uppercase

print(str2.title())# title() method is used to convert the string to title case where first character of each word is uppercase and rest are lowercase

print(str2.startswith("h"))# startswith() method is used to check if the string starts with specified substring or not and return boolean value



'''conditional statements in python'''


#if-else statement
a = int(input("Enter a number: "))
print("your age is:", a)
if a>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote") 

# if-elif-else statement
b = int(input("Enter your marks: "))
print("your marks are:", b)
if b>=90:
    print("Grade A")
elif b>=80:
    print("Grade B")
elif b>=70:
    print("Grade C")
elif b>=60:
    print("Grade D")
else:
    print("Grade F")

# nested if statement 
c = int(input("Enter your age: "))
print("your age is:", c)
if c>=18:
    print("you are eligible to vote")
    if c>=21:
        print("you are also eligible for driving license")
    else:
        print("you are not eligible for driving license")
else:
    print("you are not eligible to vote")

# multiple if statements
d = int(input("Enter your age: "))
print("your age is:", d)
if d>=18:
    print("you are eligible to vote")
if d>=21:
    print("you are eligible for driving license")
if d>=65:
    print("you are eligible for senior citizen benefits")
else:
    print("you are not eligible for senior citizen benefits")

#match case statement : 

import os
print("Current Operating System:", os.name)
os.system("python --version")

# POSIX is stands for : POSIX (Portable Operating System Interface), which is a family of standards specified by the IEEE for maintaining compatibility between operating systems.
# we can't use break statement in match case like switch case in other languages

#match case is used to match a particular value with multiple cases and based on that case we can execute a perticular block of code

x = int(input("Enter a number : "))
match x :
    case 0 : 
        print("you have entered zero")
    case _ if x > 0 :
        print("you have entered a positive number", x)
    case _ if x < 0 :
        print("you have entered a negative number", x)
    case _ :
        print("invalid input")

###LOOPS in Python

# for loop :
name = "sakshi"
for a in name : # a is variable --> which will take value from name one by one
                # name is iterable (like list , string , tuple , dictionary etc)
    print(a)
print("\n")



for i in range(5):  # it will print values from 0 to 4 (n-1)(syntax : range(n) )
    print(i)
print("\n")



for j in range( 10 ,20): # it will print values from 10 to 19 (syntax : range(start , end) )
    print(j)
print("\n")



for k in range( 1 , 20 , 5): # it will print values from 1 to 19 with a step of 2(syntax : range(start , end , step) )
    print(k)
print("\n")

# while loop :

count = 0 # initilization of variable
while count < 5 : #condition
    print("the count is : ", count)
    count += 1 # incrementing the variable 
print("\n")    
# note : if we forget to increment the variable then it will become infinite loop

print("loop ended")


count = 5 # initilization of variable
while count > 0 : #condition
    print("the count is : ", count)
    count -= 1 # decrementing the variable 
print("\n")    
# note : if we forget to increment the variable then it will become infinite loop

print("loop ended")


'''do while loop : '''
#In Python, there’s no built-in do…while loop like in C, C++, or Java — but you can emulate it easily

while True : # infinite loop
    num = int(input("Enter a number less than 5 : "))
    if num >= 5 :
        num +=1 
        print("the number is : ", num)
        break # to exit the loop

#### Break and continus statement

# break statement is used to terminate the loop
# continue statement is used to skip the current iteration of the loop and continue with the next iteration

# break statement

for i in range(1,11):

    if i == 10:
        break
    print(f"5 * {i} = {5*(i)}")


# continue statement

for i in range(11):

    if i == 5:
        continue
    print(f"6 * {i+1} = {6*(i+1)}")

### FUNCTIONS ###

#def keywords is use for desfining function in python

def greet(name): # defining a function named greet that takes one parameter, name
    """This function greets to the person passed in as a parameter""" 
    # docstring explaining what the function does
    print("Hello, " + name + ". Good morning!") 
    # prints a greeting message using the provided name

greet ("siya") # calling the greet function with the argument "siya"

#pass is use for empty function which will be implemented later

'''
-->>Parameter :: 

A parameter is the variable name listed in a function’s definition.
It acts like a placeholder for the value the function will receive.

def greet(name):   # 'name' is a parameter
    print("Hello", name)

-->>Argument ::

An argument is the actual value you pass to the function when calling it.

greet("Rai")   # "Rai" is an argument

-->>Simple difference ::

Term	    Where used?             What is it?
Parameter	In function definition	Variable/placeholder
Argument	In function call	    Actual value passed'''

# two types of functions : 1> Built-in functions 2> User-defined functions

# Built-in functions are pre-defined functions in Python like print(), len(), type(), etc.
# User-defined functions are functions created by the user to perform specific tasks, like the greet function above , using def keyword.

'''-->>Function Arguments & return statements ::'''

'''Function arguments are the values you pass to a function when you call it.

there are four types of function arguments in Python:
1. Default arguments
2. Keyword arguments
3. variable-length arguments
4. Required arguments  


1. Default Arguments ::These are arguments that assume a default value if a value is not provided in the function call.

'''

#example of default argument :: 

def avg(a , b):
    c = (a + b) / 2
    return c

result = avg(6,6)
print(result)
#output : 6.0


'''

def aveg(a, b):
    c = (a + b) / 2
    return c

aveg(6, 6)


This calculates the average of 6 and 6.

🔹 If you use return
def aveg(a, b):
    c = (a + b) / 2
    return c

result = aveg(6, 6)
print(result)


✅ What happens:

The function sends the value back to where it was called.

You can store it, use it in calculations, pass it to another function, etc.

Here, result will be 6.0.

👉 return = give the value back to the caller.

🔹 If you use print instead
def aveg(a, b):
    c = (a + b) / 2
    print(c)

result = aveg(6, 6)
print(result)


✅ What happens:

The function just displays the value on the screen.

It does not send it back.

By default, the function returns None.

Output:

6.0
None


👉 print = only show the value, don’t give it back.

⚖️ Key Difference (Simple Table)
return	print
Sends value back from function	Only shows value on screen
Can be stored in a variable	Cannot be stored/used later
Used for computation & logic	Used for display/debugging
Ends the function execution	Function continues (if code left)
🧠 In very simple words:

return → “Here is the result, you can use it.”

print → “Look at this result on the screen.”

📌 Rule of thumb

Use return when you want the function’s result for further use.

Use print when you just want to display something to the user.

So for your average function, return is the correct choice if you want to actually use the average value elsewhere.'''

#required arguments ::
def multiply(x, y=4):  # x and y are required parameters
    return x * y

result = multiply(5)  # both arguments must be provided
print(result)  # Output: 20

#variable-length arguments ::
def sum_all(*args):  # *args allows for variable number of arguments
    print(type(args))  # Output: <class 'tuple'>
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

sum_all(1, 2, 3, 4, 5)  # Output: Sum: 15