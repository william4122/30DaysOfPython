# Strings

- Text is a string data type.
- Any data type in text is a string
- Single, double, triple quotes are strings
- have different methods/built in functions to deal with strings
- len() method gives you the length of a string

## Creating a string

- Creating a string is as simple as declaring a variable and assigning it the string data type 

>>> letter='P'
>>> print(letter)
P
>>> print(len(letter))
1
>>> greeting='Hello World! This is Will!'
>>> print(greeting)
Hello World! This is Will!
>>> print(len(greeting))
26
>>> sentence='I hope you enjoy this challenge while you put in the work!' 
>>> print(sentence)
I hope you enjoy this challenge while you put in the work!

- Just like you make a multiline comment with ''' or with """ you also make a multiline string with triple quotes

multiline_string= '''Can you believe that my birthday was almost a whole week ago?
I had so much fun during my birthday weekend!
I can't wait to get my shoe back'''

>>> multiline_string= '''Can you believe that my birthday was almost a whole week ago?I had so much fun during my birthday weekend!I can't wait to get my shoe back'''
>>> print(multiline_string)
Can you believe that my birthday was almost a whole week ago?I had so much fun during my birthday weekend!I can't wait to get my shoe back

## String Concatenation

- Connecting/merging strings together is called concantenation:
>>> first_name='Will'
>>> last_name='Rodriguez'
>>> space=' ' 
>>> full_name= first_name + space + last_name
>>> print(full_name)
Will Rodriguez
>>> print(len(first_name))
4
>>> print(len(last_name))
9
>>> print(len(first_name) > len(last_name))
False
>>> print(len(full_name))
14

## Escape Sequences in Strings

- \ followed by a character is an escape sequence. Most common escape characters

\n: new line
\t: tab means (8 spaces)
\\: Back slash
\': Single quote '
\": double quote "

>>> print('Are you enjoying this challenge? \n I am!') 
Are you enjoying this challenge?
 I am!
>>> print('Days\tTopics\tExercises')
Days    Topics  Exercises
>>> print('Day 1\t5\t5')
Day 1   5       5
>>> print('Day 2\t6\t20')
Day 2   6       20
>>> print('Day 3\t5\t23')
Day 3   5       23
>>> print('Day 4\t1\t35')
Day 4   1       35
>>> print('This is a backslash symbol (\\)')
This is a backslash symbol (\)
>>> print('In every programming language it starts with \"Hello, World!\"')
In every programming language it starts with "Hello, World!"

## String formatting

- Python has many ways of formatting strings, this section goes over a couple of them

### old style string formatting (% operator)

% formats a set of variables enclosed in a tuple (a fixed size list), together with a format string, containing normal text together with "argument specifiers"

%s - string or any object that can be represented with a string like #'s for example
%d - integers
%f - floating point
"%.number of digits" - floating point w. fixed precision 

>>> #Strings only
>>> first_name='Will'                                                          
>>> last_name='Rodriguez'
>>> language='Python'
>>> formatted_string='I am %s %s. I teach %s' %(first_name, last_name, language)  
>>> print(formatted_string)                                                      
I am Will Rodriguez. I teach Python

>>> #Strings and numbers
>>> radius = 10 
>>> pi = 3.14
>>> area = pi * radius ** 2
>>> formatted_string= 'The area of a circle with radius %d is %.2f.' %(radius, area)
>>> print(formatted_string)
The area of a circle with radius 10 is 314.00.

>>> python_libraries = ['Django','Flask','NumPy','Matplotlib','Pandas']
>>> formatted_string='The following are python libraries: %s' % (python_libraries) 
>>> print(formatted_string)
The following are python libraries: ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']

### new style string formatting (str.format)

>>> first_name='Will'
>>> last_name='Rodriguez'
>>> job='AV/EDR Support L2'
>>> formatted_string= 'I am {} {}. I work at Kaseya as a {}'.format(first_name, last_name, job)
>>> print(formatted_string)
I am Will Rodriguez. I work at Kaseya as a AV/EDR Support L2

>>> a=4
>>> b=3
>>> print('{} + {} = {}'.format(a, b, a+b))
4 + 3 = 7
>>> print('{} - {} = {}'.format(a, b, a-b)) 
4 - 3 = 1
>>> print('{} * {} = {}'.format(a, b, a*b)) 
4 * 3 = 12
>>> print('{} / {}'.format(a, b, a/b))
4 / 3
>>> print('{} / {} = {}'.format(a, b, a/b)) 
4 / 3 = 1.3333333333333333
>>> print('{} % {} = {}'.format(a, b, a%b))
4 % 3 = 1
>>> print('{} // {} = {}'.format(a, b, a//b))
4 // 3 = 1
>>> print('{} ** {} = {}'.format(a, b, a **b))
4 ** 3 = 64

>>> #Strings and numbers
>>> radius = 10 
>>> pi = 3.14
>>> area = pi * radius ** 2
>>> formatted_string='The area of a circle with radius {} is {:.2f}.'.format(radius, area)
>>> print(formatted_string)
The area of a circle with radius 10 is 314.00.

### string interpolation / f-Strings (python 3.6+)

- Strings start with f and we inject the data in their positions

>>> a=4
>>> b=7
>>> print(f'{a} + {b} = {a+b}')
4 + 7 = 11
>>> print(f'{a} - {b} = {a-b}')
4 - 7 = -3
>>> print(f'{a} * {b} = {a*b}')
4 * 7 = 28
>>> print(f'{a} / {b} = {a / b:.2f}')
4 / 7 = 0.57
>>> print(f'{a} % {b} = {a % b}')
4 % 7 = 4
>>> print(f'{a} // {b} = {a // b}')  
4 // 7 = 0
>>> print(f'{a} ** {b} = {a ** b}')
4 ** 7 = 16384

## Python Strings as Sequences of Characters

- Strings are just sequences of characters, they share basic methods of access with other ordered objects in python - like lists/tuples
- Simplest way of extracting individual memebers from any sequence is unpacking them into corresponding variables 

### Unpacking characters

>>> language = 'Spanish' 
>>> a,b,c,d,e,f,g=language
>>> print(a)
S
>>> print(b)
p
>>> print(c)
a
>>> print(d)
n
>>> print(e)
i
>>> print(f)
s
>>> print(g)
h

### Accessing chracters in string by index

- Counting starts from 0 therefore the first letter of a string is 0 index, 

>>> restaurant='Sushi Sake'
>>> first_letter = restaurant[0]
>>> print(first_letter)
S
>>> second_letter=restaurant[1]
>>> print(second_letter)
u
>>> last_index = len(restaurant) - 1
>>> last_letter = restaurant[last_index]
>>> print(last_letter)
e

### Slicing python strings

>>> gym= 'LA-Fitness'  
>>> first_four=gym[0:4]      
>>> print(first_four)  
LA-F
>>> #Another way of printing with negative indexing
>>> last_three = gym[-3:]
>>> print(last_three)
ess
>>> last_three =gym[3:]
>>> print(last_three)
Fitness

### Reversing a string

- You can reverse a string in python
>>> greeting='Hello from Wills World!'
>>> print(greeting[::-1])
!dlroW slliW morf olleH

### Skipping chracters while slicing

- You can pass a argument to the slice method and pick out certain characters

>>> language='python'
>>> pto=language[0:6:2]
>>> print('I need my',pto)  
I need my pto

## String Methods

- There are many methods we can use to format strings, here are some examples: 

1. capitalize(): converts first character of string to capital letter

>>> dance='ella quiere beber'
>>> print(dance.capitalize())
Ella quiere beber

2. count(): returns occurences of the subctring in string. 

