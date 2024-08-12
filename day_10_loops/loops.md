# Loops

- To handle repetetive taks in programming we use a loop. 

Python provides us the following types of two loops:

1. while loop
2. for loop 

## While Loops

- while = reserved word in python
- execute a block of statements until a condition is satisfied; when the condition becomes false, the lines of code after the loop will continue to execute

```
#general syntax for a while loop
while condition:
    code goes here

#example of a while loop

count = 0
while count < 5:
    print(count)
    count = count + 1
>>
0
1
2
3
4
```

- In the above example, the condition is false when the count is equal to 5, the loop stops; and then executes the else statement. 

## Break and Continue - Part 1

- Break: you can use a break when you want to get out/stop a loop 

```
#General syntax for  while loop with a break statement
while condition:
    code goes here
    if another_condition:
        break

#Example that involves breaking the loop
count=0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
0
1
2
```
- The above example breaks when count reaches 3

- Continue: skip the current iteration and continue with the next 

```
#general syntax for a while loop with a continue statement
while condition:
    code goes here
    if another_condition:
        continue

#an example of this
count=0
while count < 5:
    if count ==3:
        count = count + 1
        continue
    print(count)
    count = count + 1
0
1
2
4
```
- This example above pnly prints 0,1,2,4 and skips 3

## For Loop

- for keyword is used to make a for loop, used to iterate over a sequence (either list, tuple, dictionary, set, string)
 
- for loop with list:

```
#general syntax of a for loop with list
for iterator in lst:
    code goes here

#example
numbers=[0,1,2,3,4,5]
for number in numbers: #number is temp to refer list items, only valid inside of this loop 
    print(number)
0
1
2
3
4
5   
```

- for loop with string:

```
# general syntax of a for loop with string
for iterator in string:
    code goes here
# actual example:
language='Python'
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])
P
y
t
h
o
n
P
y
t
h
o
n
```

- for loop with tuple:

```
# general syntax of a for loop with tuple
for iterator in tpl:
    code goes here
#example:
numbers=(0,1,2,3,4,5)
for number in numbers:
    print(number)
0
1
2
3
4
5
```

- for loop with dictionary
    - looping through a dictionary gives you the keys of the dictionary

```
# general syntax of a for loop with a dictionary
for iterator in dct:
    code goes here

#example:
person = {
    'first_name':'Will',
    'last_name':'Rodriguez',
    'age':260,
    'country':'USA',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Wills world',
        'zipcode':'99135'
    }
}

# in this example the key is the iterator
for key in person:
    print(key)
first_name
last_name
age
country
is_marred
skills
for key, value in person.items():
    print(key, value) #This will print both the key/values
first_name Will
last_name Rodriguez
age 260
country USA
is_marred False
skills ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
address {'street': 'Wills world', 'zipcode': '99135'}
```

- for loops with a set 

```
#general syntax for loops with a set
for iterator in st:
    code goes here

#example:
it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
for company in it_companies:
    print(company)
Facebook
IBM
Amazon
Oracle
Apple
Google
Microsoft
```
## Break and Continue - Part 2 

- Break: use break when you want to stop a loop before it completes
- in the example below the loop stops when it reaches to 3
```
#general syntax for break
for iterator in sequence:
    code goes here
    if condition:
        break

#example:
numbers=(0,1,2,3,4,5,6,)
for number in numbers:
    print(number)
    if number == 3:
        break
0
1
2
3
```

Continue: skip some of the steps in the iteration of the loop 
- In the example, if the number equals 3 the step after the condition but inside the loop is skipped and the execution continues if there are iterations left 

```
#general syntax of a loop with continue statement
for iterator in sequence:
    code goes here
    if condition:
        continue
#actual example:
numbers=(0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")
print('Outside the loop')
0
Next number should be  1
1
Next number should be  2
2
Next number should be  3
3
4
Next number should be  5
5
loop's end
Outside the loop
```

## The Range Function

-  range() function is used in lists of numbers
    - this function has 3 parameters range(start, end, step)
        - by default: starts from 0 and increments in 1
        - needs at least one argument/parameter (end)

```
#general syntax of range:
for iterator in range(start, end, step):

#example of range function
for number in range(11):
    print(number)
0
1
2
3
4
5
6
7
8
9
10

#example of creating sequences using the range function 
lst=list(range(11))
print(lst)
st=set(range(1,11))
print(st)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst)
st = set(range(0,11,2))
print(st)
[0, 2, 4, 6, 8, 10]
{0, 2, 4, 6, 8, 10}
```

## Nested For Loop 

- It is possible to write loops inside of loops

```
#general syntax of nested for loops

for x in y:
    for t in x:
        print(t)

#example
person = {
    'first_name':'Will',
    'last_name':'Rodriguez',
    'age':260,
    'country':'USA',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Wills world',
        'zipcode':'99135'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
JavaScript
React
Node
MongoDB
Python
```

## For Else

- If you want to execute some message when the loop ends, use else 

```
#general syntax 

for iterator in range(start,end,step):
    do something
else:
    print('The loop ended')

#example:
for number in range(11):
    print(number)
else:
    print('The loop stops at', number)
0
1
2
3
4
5
6
7
8
9
10
The loop stops at 10
```

## Pass

- When statement is required (after semicolon) but we don't want to execute code there, we write the word pass to avoid eny errors; can also be used as a placeholder for a future statement

```
for number in range(6):
    pass
<does nothing>
```
