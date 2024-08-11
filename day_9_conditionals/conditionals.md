# Conditionals
----------------
- Statements in python are executed sequentially top -> bottom 
- Sequential flow of execution can be altered in two ways
    1. Conditional execution - block of one or more statements that will be executed if certain expression is true 
    2. Repetitive execution - block of one or more statements that will be repetively executed as long as a certain expression is true
        - if, else, elif statements; comparison & logical operators are useful here

To recap: 

Comparison Operators
either return a true or false so boolean data type 
== equal x==y
!= not equal x!=y
> greater than
< less than 
>= greater than or equal to 
<= lesser than or equal to 

other comparison operators:
is: returns true if both variables are the same object (x is y)
is not: returns true if both variables are not the same object (x is not y)
in: returns true if queried list contains a certain item (x in y)
not in: returns true if the queried list doesn't have a certain item (x not in y)

Logical Operators
operator :: description :: example
and :: true if both statements are true :: x < 5 & x < 10 
or :: true if one statement is true :: x <5  or x < 4
not: returns false if the result is true :: not (x <5 and x <10)

## If Condition
----------------

- If is used to check if something is true and if so, execute the code block.
- Needs an indentation after the colon

```
>>> #syntax
>>> if condition:
... this part of code runs for truthy conditions
>>> a=3
>>> if a > 0:   
...     print('A is a positive number')
A is a positive number
```

- If the condition was false and a was a negative number we would not see the code execute/result. 

## If Else
----------

- If condition is true, execute the first block, if not the 2nd block will run

```
if condition:
    this part of the code runs for true conditions
else:
    this part runs for false conditions

a=3
if a <0:
    print('A is a negative number')
else:
    print('A is a positive number')
A is a positive number   
```

## If Elif Else
----------------
- When we check multiple conditions in python to make a decision we use elif statements

```
#syntax
if condition:
    code
elif condition:
    code
else:
    code
#Example
a=0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
>>>A is zero
```

## Short Hand
--------------

- How to write a conditional in short hand 

```
>>> a=3
>>> print('A is positive') if a > 0 else print('A is negative')
A is positive
```

## Nested Conditions
---------------------

- Conditions can be nested 
- If you want to avoid nested conditions, consider the use of the logical operator and

```
#syntax
if condition:
    code
    if condition:
    code

Example. 
a=o
if a > 0:
    if a % 2 == 0
        print('A is positive and even integer')
    else:
        print('A is positive number')
elif a -- 0:
    print('A is zero')
else:
    print('A is a negative number')
```

## If Condition and Logical Operators
--------------------------------------

```
if condition and condition:
    code
```

Example:
```
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
>>> A is zero
```

## If and Or Logical Operators
-------------------------------

- What about an if condition with an Or logical operator 

```
#example
if condition or condition:
    code

#Example
user='Will'
access_level=3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
>>> Access denied!
```