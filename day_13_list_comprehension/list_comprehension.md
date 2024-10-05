# List Comprehension

- List comprehension is compact way of creating lists from a sequence
- Short way to create new list
- List comprehension is faster than processing a list with a FOR loop 

```
#syntax
[i for i in iterable if expression]
```

### Example 1
- Change a string to a list of characters

```
language='Python'
lst = list(language)
print(type(lst))   
<class 'list'>
print(lst)
['P', 'y', 't', 'h', 'o', 'n']

#Second way
lst=[i for i in language]
print(type(lst))
<class 'list'>
print(lst)
['P', 'y', 't', 'h', 'o', 'n']
```

### Example 2
- If you want to generate a list of numbers

```
#Generating numbers
numbers = [i for i in range(11)]
print(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Its possible to math operations during the iteration
squares = [i * i for i in range(11)]
print(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#It is also possible to make a list of tuples
numbers=[(i, i*i) for i in range(11)]
print(numbers)
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
```

### Example 3

- List comprehension can be combined with if expression
```
 #generating even numbers
 even_numbers=[i for i in range(21) if i % 2 == 0] # to generate even numbers list in range 0 - 21 
 print(even_numbers)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

 #generating odd numbers
 odd_numbers = [i for i in range(21) if i % 2 != 0] # to generate odd numbers list in range 0 -21 
 print(odd_numbers)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

 #flattening a three dimensional array
 list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
 flattened_list = [number for row in list_of_lists for number in row]
 print(flattened_list)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
# Lambda Function

- Lamdas are small anonymous functions without a name
- Can take any number of arguments but only has one expression
- Similar to anonymous functions in JS
- We use it when we create an anonymous function inside another funciton 

## Creating a Lambda Function

- We create a lambda function by using the lambda keyword followed by parameters, then an expression
-Lambdas do not use the word return in them, they explicitly return the expression

```
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

### Example
```
# Named function
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))     # 5

add_two_nums = lambda a,b: a + b 
print(add_two_nums(2,3))
5
#self invoking lambda function
(lambda a, b: a + b)(2,3)
5

#multiple-variables-with-lambda-functions
    
multiple_variable = lambda a, b, c: a ** 2 -3 / b + 4 * c
print(multiple_variable(5,5,3))
36.4
```

## Lambda Function Inside Another Function

- We can use lambda functions inside of other functions

```
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
32
```
