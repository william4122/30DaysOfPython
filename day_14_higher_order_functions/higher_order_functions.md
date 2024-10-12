# Higher Order Functions
- Functions are treated as first class citizens in python, we can do the following on them:
    - Functions can take one or more functions as parameters
    - Function can be returned as a result of another function
    - Functions can be modified
    - Functions could be assigned to a variable

## Function as a parameter
How to handle a function as a parameter

```
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst)
    summation = f(lst)
    return summation
result = higher_order_function(sum_number, [1,2,3,4,5])
print(result)
```
- in this code block above we have a higher order function called higher_order_function because it takes a function, f as a parameter, and in this example we passed it the sum_number function as one of the parameters. 

## Function as a return value

```
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

#this is our higher order function which returns another function as its result
#now we'll use this function to return other functions we assign a variable too and get a result from

result = higher_order_functions('square')
print(result(3))
#9

result = higher_order_functions('cube')
print(result(3))
#27

result = higher_order_functions('absolute')
print(absolute(-3))
#3
```

# Closures

- Nested function to access the outer scope of an enclosing function = closure
- Closures are created in python by nesting a function inside another encapsulating function & returning the inner function

```
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result= add_ten()

print(closure_result(5))
#15

print(closure_result(10))
#20
```

# Decorators

- Decorators = design pattern which allow users to add new functionality to an existing object without modifying its structure.
    - Called before the definition of the function you want to decorate 

## Creating Decorators

- To create a decorator, you need an outer function with an inner wrapper function

```
# Normal greeting
def gretting():
    return 'Welcome to WIlls World'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Wills World'
print(greeting()) # WELCOME TO WILLS WORLD
```

## Applying Multiple Decorators to a Single Function

- *Decorator functions are higher order functions that take functions as parameters*

```
#First decorator
def uppercase_decorator(function):
    def wrapper()
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

#Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator
#order with decorators is important, .upper() does not work with lists 
def greeting():
    return 'Welcome to Wills World'
print(greeting()) # WELCOME TO WILLS WORLD
```

## Accepting Parameters in Decorator Functions

- If a function needs to take parameters, so its possible to define a decorator that accepts parameters

```
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name, country))

print_full_name("William", "Rodriguez",'Miami')
```
# Built-in Higher Order Functions

- some of the higher order functions covered here are: map(), filter, reduce
- lambda functions can be passed as parameters
    - *Best use case for lambda functions is in functions like these*

## Map Function

- built in function that takes a function and iterable as parameters

```
#syntax
map(function,iterable)
```

### Example 1

```
numbers = [1,2,3,4,5] #iterable a list to 5 
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))
 # [1, 4, 9, 16, 25]

#Now lets try it but with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))
# [1, 4, 9, 16, 25]
```

### Example 2 

- I thought this was a crafty way of going from a list of strings of numbers, to an integer list of numbers 

```
numbers_str = ['1','2','3','4','5'] #iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))
# [1, 2, 3, 4, 5]
```

### Example 3: 

- Goes over a list and makes an operation to it. Capitalize

```
names = ['Will','Matt','Kevin','Angel'] #iterable. a list of strings[names]

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)

print(list(names_upper_cased))
#['WILL','MATT','KEVIN','ANGEL']

#we can also apply this with a lambda function
names_upper_cased = map(lambda name : name.upper(), names)
print(list(names_upper_cased))
#['WILL','MATT','KEVIN','ANGEL']
```

- It iterates over a list 

## Filter Function

- The filter() function calls specified function which returns boolean for each item in the iterable (list).
    - Filters the items that satisfy the criteria 

```
#syntax
filter(function, iterable)
```

### Example 1: Filter even numbers out

```
# filter only even numbers
numbers = [1,2,3,4,5]

def is_even(num):
    if num % 2 == 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))
# [1,3,5]
```
### Example 2: Filter a long name

```
names = ['Will','Matt','Kevin','Angel'] 
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))
```

## Reduce Function

- reduce function is defined in the functools module and we should import it from this module

- it takes two parameters: a function & iterable

- it does not return a another iterable it returns a single value

### Example 1: 

```
numbers_str = ['1','2','3','4','5']
def add_two_nums(x,y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)
#15
```
