# Functions

- We have seen a good amount of the built-in python functions through this class, but what is a function and why do we use them in python?

## Declaring a function

- Functions are reusable blocks of code designed to perform certain task

- To declare a function we use the def keyword 

- We only execute functions that we call or invoke

## Declaring and calling a function

- When we make functions that is called declaring a function
    - Can be declared with or without parameters
- When we use the function, is called (calling or invoking) the function

```
def function_name():
    codes
    codes
# Calling a function
function_name()
```

## Functions without parameters

Functions can be declared without parameters.

An example of a function that prints my full name 

```
def generate_full_name():
    first_name= 'Will'
    last_name = 'Rodriguez'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()
Will Rodriguez
```

An example of a function that adds two numbers

```
def add_two_numbers ():
    num_one= 3
    num_two= 4
    total = num_one + num_two
    print(total)
add_two_numbers()
7
```

## Functions with parameters
- We can pass the different data types in a function as a parameter (number, string, boolean, list, tuple, dictionary, set)

    - Single parameter: if the function takes a parameter you should call the function with that argument
```
        # syntax
        # Declaring a function
         def function_name(parameter):
            codes
            codes
        # Calling function
        print(function_name(argument))
```

Example:

```
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Will'))
Will, welcome to Python for Everyone!

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))
100

def square_number(x):
    return x * x 
print(square_number(2))
4

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Two Parameter: function may or may not have a parameter, function could even have two paramters, if the function takes parameters, you should call them with arguments. 

**generic example**

```
def function_name(para1, para2):
    codes
    codes
# calling function
print(function_name(arg1, arg2))
```

**actual examples**
```
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Will', 'Rodriguez'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two 
    return sum
print('Sum of two numbers: ', sum_two_numbers(1,9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Your current age is ', calculate_age(2024,1998))

def weight_of_object (mass, gravity):
    weight= str(mass * gravity)
    return weight
print('Weight of an object in Newtons:', weight_of_object(100, 9.81))
```

## Functions Returning a Value - Part 1 

- Functions can return values, if a function does not a return statement then the value of the function is none. Looking at the functions we wrote previously, lets incorporate return statements into them

```
def generate_full_name():
    first_name= 'Will'
    last_name = 'Rodriguez'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
Will Rodriguez
```

```
def add_two_numbers ():
    num_one= 3
    num_two= 4
    total = num_one + num_two
    return total
print(add_two_numbers())
7
```

## Functions Returning a Value - Part 2 

- Functions return none when they output a value
-We can return any kind of data type from a function

**Examples**

1. String

def print_name(firstname):
    return firstname
print_name('Will')

def print_full_name(firstname, lastname)
    space = ' ' 
    full_name = firstname + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')

2. Number

```
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year)
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
```

3. Boolean
```
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True
    return False
print(is_even(10))
print(is_even(7))
```

4. List

```
def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
[0, 2, 4, 6, 8, 10]
```

## Passing arguments with key and value

- If you explicityly define the key(paramater_name) and value(parameter_value or argument) when calling the function, the order of the parameters does not matter

**Generic Example**

```
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
```

**Specific Examples**

```
def print_full_name(firstname, lastname):
    space = ' ' 
    full_name = firstname + space + lastname
    print(full_name)
(print_full_name(lastname= 'Rodriguez', firstname = 'Will'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
```

## Functions with Default Parameters

- If we pass default values to the parameters of a function; when this function is invoked and no arguments are passed when calling the function the default values will be used 

**Generic Example**
```
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

**Example**
```
def greetings (name  = 'Will'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Greg'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('Will', 'Rodriguez'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
```

## Arbitrary number of arguments

- If you don't know how many arguments you should pass a function you can create a function which takes arbitary number of arguments by adding * before the parameter  name 

**Generic Example**
```
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

**Example**
```
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

## Default Arbitrary Number of Parameters in Functions

- Example of including both a argument in function declaration as well as adding the arbitrary number of arguments after, we need to give this function a team argument 

```
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))
```

## Functions as a Parameter of Another Function

- We can pass functions to other functions as parameters

**Example**

```
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```